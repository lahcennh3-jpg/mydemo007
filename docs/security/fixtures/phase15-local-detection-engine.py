import argparse
import json
import pathlib


def load_json(path):
    return json.loads(
        pathlib.Path(path).read_text()
    )


def load_jsonl(path):
    return [
        json.loads(line)
        for line in pathlib.Path(path)
        .read_text()
        .splitlines()
        if line.strip()
    ]


def prohibited_keys(schema):
    return set(
        schema[
            "sensitive_log_policy"
        ][
            "prohibited"
        ]
    )


def validate_event(event, schema):
    required = set(
        schema[
            "required_event_fields"
        ]
    )

    missing = (
        required
        -
        set(event)
    )

    if missing:
        raise ValueError(
            "MISSING_REQUIRED_FIELDS:"
            +
            ",".join(
                sorted(missing)
            )
        )

    forbidden = (
        set(event)
        &
        prohibited_keys(schema)
    )

    if forbidden:
        raise ValueError(
            "PROHIBITED_EVENT_KEYS:"
            +
            ",".join(
                sorted(forbidden)
            )
        )

    if event.get(
        "synthetic"
    ) is not True:
        raise ValueError(
            "NON_SYNTHETIC_EVENT_REJECTED"
        )


def requirement_map(requirements):
    return {
        item["id"]: item
        for item
        in requirements[
            "detections"
        ]
    }


def alert_for(
    event,
    detection_id,
    requirements,
    correlated_event_ids=None,
):
    rule = requirements[
        detection_id
    ]

    correlated_event_ids = (
        correlated_event_ids
        or
        [event["event_id"]]
    )

    return {
        "alert_id":
            "ALERT-"
            + event["event_id"]
            + "-"
            + detection_id,

        "detection_id":
            detection_id,

        "detection_name":
            rule["name"],

        "severity":
            rule["severity"],

        "event_id":
            event["event_id"],

        "trace_id":
            event["trace_id"],

        "actor_id":
            event["actor_id"],

        "actor_tenant":
            event["actor_tenant"],

        "resource_tenant":
            event["resource_tenant"],

        "source":
            event["source"],

        "result":
            event["result"],

        "correlated_event_ids":
            correlated_event_ids,

        "synthetic":
            True,
    }


def run_engine(
    events,
    schema,
    requirements_document,
    policy,
):
    rules = requirement_map(
        requirements_document
    )

    alerts = []

    prompt_security_by_trace = {}

    injection_classes = set(
        policy[
            "prompt_security_classifications"
        ]
    )

    thresholds = policy[
        "resource_thresholds"
    ]

    for event in events:
        validate_event(
            event,
            schema,
        )

        event_type = event[
            "event_type"
        ]

        trace_id = event[
            "trace_id"
        ]

        # ----------------------------------------------------
        # Security signal state for later cross-event
        # correlation.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "prompt_security_signal"
            and
            event.get(
                "prompt_security_classification"
            )
            in injection_classes
        ):
            prompt_security_by_trace[
                trace_id
            ] = event[
                "event_id"
            ]


        # ----------------------------------------------------
        # D15-001
        # Cross-tenant authorization attempt.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "authorization_decision"
            and
            event.get(
                "actor_tenant"
            )
            !=
            event.get(
                "resource_tenant"
            )
        ):
            alerts.append(
                alert_for(
                    event,
                    "D15-001",
                    rules,
                )
            )


        # ----------------------------------------------------
        # D15-002
        # Privilege / service identity anomaly.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "privileged_action"
            and
            event.get(
                "baseline"
            )
            ==
            "not_expected"
        ):
            alerts.append(
                alert_for(
                    event,
                    "D15-002",
                    rules,
                )
            )


        # ----------------------------------------------------
        # D15-003
        # Prompt injection correlated with tool execution.
        # Supports both:
        #   - same-event classification;
        #   - prior event with same trace_id.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "tool_call"
        ):
            inline_injection = (
                event.get(
                    "prompt_security_classification"
                )
                in
                injection_classes
            )

            previous_injection = (
                trace_id
                in
                prompt_security_by_trace
            )

            if (
                inline_injection
                or
                previous_injection
            ):
                correlated = [
                    event[
                        "event_id"
                    ]
                ]

                if previous_injection:
                    correlated.insert(
                        0,
                        prompt_security_by_trace[
                            trace_id
                        ],
                    )

                alerts.append(
                    alert_for(
                        event,
                        "D15-003",
                        rules,
                        correlated,
                    )
                )


        # ----------------------------------------------------
        # D15-004
        # Unexpected runtime / tool destination.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "runtime_destination"
            and
            event.get(
                "allowlist_decision"
            )
            ==
            "deny"
        ):
            alerts.append(
                alert_for(
                    event,
                    "D15-004",
                    rules,
                )
            )


        # ----------------------------------------------------
        # D15-005
        # Retrieval provenance anomaly.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "retrieval"
            and
            (
                event.get(
                    "provenance_status"
                )
                !=
                "verified"
            )
        ):
            alerts.append(
                alert_for(
                    event,
                    "D15-005",
                    rules,
                )
            )


        # ----------------------------------------------------
        # D15-006
        # DLP block / telemetry gap.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "dlp_decision"
            and
            (
                event.get(
                    "dlp_decision"
                )
                ==
                "block"
                or
                (
                    event.get(
                        "telemetry_expected"
                    )
                    is True
                    and
                    event.get(
                        "telemetry_observed"
                    )
                    is False
                )
            )
        ):
            alerts.append(
                alert_for(
                    event,
                    "D15-006",
                    rules,
                )
            )


        # ----------------------------------------------------
        # D15-007
        # Unapproved security configuration change.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "configuration_change"
            and
            event.get(
                "approval_status"
            )
            !=
            "approved"
        ):
            alerts.append(
                alert_for(
                    event,
                    "D15-007",
                    rules,
                )
            )


        # ----------------------------------------------------
        # D15-008
        # Security behavior drift.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "security_behavior_metric"
            and
            isinstance(
                event.get(
                    "observed_value"
                ),
                (int, float),
            )
            and
            isinstance(
                event.get(
                    "threshold"
                ),
                (int, float),
            )
            and
            event[
                "observed_value"
            ]
            <
            event[
                "threshold"
            ]
        ):
            alerts.append(
                alert_for(
                    event,
                    "D15-008",
                    rules,
                )
            )


        # ----------------------------------------------------
        # D15-009
        # Resource / economic anomaly.
        # ----------------------------------------------------

        if (
            event_type
            ==
            "resource_usage"
        ):
            exceeded = any(
                event.get(
                    key,
                    0,
                )
                >
                thresholds[
                    key
                ]
                for key
                in (
                    "token_count",
                    "tool_call_count",
                    "recursion_depth",
                    "concurrency",
                    "cost_units",
                )
            )

            if exceeded:
                alerts.append(
                    alert_for(
                        event,
                        "D15-009",
                        rules,
                    )
                )

    return alerts


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--correlation",
        required=True,
    )

    parser.add_argument(
        "--requirements",
        required=True,
    )

    parser.add_argument(
        "--policy",
        required=True,
    )

    parser.add_argument(
        "--events",
        required=True,
    )

    parser.add_argument(
        "--output",
        required=True,
    )

    args = parser.parse_args()

    schema = load_json(
        args.correlation
    )

    requirements = load_json(
        args.requirements
    )

    policy = load_json(
        args.policy
    )

    events = load_jsonl(
        args.events
    )

    alerts = run_engine(
        events,
        schema,
        requirements,
        policy,
    )

    output_path = pathlib.Path(
        args.output
    )

    output_path.write_text(
        "".join(
            json.dumps(
                alert,
                sort_keys=True,
            )
            +
            "\n"
            for alert
            in alerts
        )
    )

    print(
        f"EVENTS_PROCESSED="
        f"{len(events)}"
    )

    print(
        f"ALERTS_GENERATED="
        f"{len(alerts)}"
    )

    print(
        "NETWORK_CALLS=0"
    )

    print(
        "RESULT=DETECTION_ENGINE_PASS"
    )


if __name__ == "__main__":
    main()
