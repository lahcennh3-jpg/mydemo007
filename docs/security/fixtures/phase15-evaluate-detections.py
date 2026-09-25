import importlib.util
import json
import pathlib
import sys


(
    engine_path,
    correlation_path,
    policy_path,
    source_events_path,
    alerts_path,
    negative_alerts_path,
    cross_alerts_path,
    metrics_path,
) = sys.argv[1:]


def read_json(path):
    return json.loads(
        pathlib.Path(path).read_text()
    )


def read_jsonl(path):
    p = pathlib.Path(path)

    if not p.exists():
        return []

    return [
        json.loads(line)
        for line
        in p.read_text().splitlines()
        if line.strip()
    ]


spec = importlib.util.spec_from_file_location(
    "phase15_engine",
    engine_path,
)

engine = importlib.util.module_from_spec(
    spec
)

spec.loader.exec_module(
    engine
)

schema = read_json(
    correlation_path
)

policy = read_json(
    policy_path
)

events = read_jsonl(
    source_events_path
)

alerts = read_jsonl(
    alerts_path
)

negative_alerts = read_jsonl(
    negative_alerts_path
)

cross_alerts = read_jsonl(
    cross_alerts_path
)


# ============================================================
# Expected vs observed
# ============================================================

expected = {
    (
        event["event_id"],
        event["expected_detection_id"],
    )
    for event
    in events
    if "expected_detection_id"
    in event
}

actual = {
    (
        alert["event_id"],
        alert["detection_id"],
    )
    for alert
    in alerts
}

tp = len(
    expected
    &
    actual
)

fp = len(
    actual
    -
    expected
)

fn = len(
    expected
    -
    actual
)

positive_event_ids = {
    event_id
    for event_id, _
    in expected
}

benign_events = [
    event
    for event
    in events
    if event["event_id"]
    not in positive_event_ids
]

alert_event_ids = {
    alert["event_id"]
    for alert
    in alerts
}

benign_alert_events = [
    event["event_id"]
    for event
    in benign_events
    if event["event_id"]
    in alert_event_ids
]

tn = (
    len(benign_events)
    -
    len(benign_alert_events)
)

precision = (
    tp / (tp + fp)
    if (tp + fp)
    else 1.0
)

recall = (
    tp / (tp + fn)
    if (tp + fn)
    else 1.0
)

expected_alert_match_rate = (
    tp
    /
    len(expected)
    if expected
    else 1.0
)


# ============================================================
# Cross-event correlation
# ============================================================

cross_event_pass = (
    len(cross_alerts) == 1
    and
    cross_alerts[0][
        "detection_id"
    ] == "D15-003"
    and
    cross_alerts[0][
        "event_id"
    ] == "E15-C202"
    and
    "E15-C201"
    in
    cross_alerts[0][
        "correlated_event_ids"
    ]
)


# ============================================================
# Missing telemetry / required field rejection
# ============================================================

missing_required_field_rejected = False

invalid_missing = {
    "timestamp":
        "2026-01-15T13:00:00Z",
    "event_id":
        "E15-INVALID-001",
    "event_type":
        "authorization_decision",
    # trace_id deliberately missing
    "actor_id":
        "user-test",
    "actor_tenant":
        "tenant-alpha",
    "resource_tenant":
        "tenant-alpha",
    "result":
        "allow",
    "source":
        "api",
    "synthetic":
        True,
}

try:
    engine.validate_event(
        invalid_missing,
        schema,
    )
except ValueError:
    missing_required_field_rejected = True


# ============================================================
# Sensitive-key rejection
# ============================================================

sensitive_key_rejected = False

invalid_sensitive = {
    "timestamp":
        "2026-01-15T13:01:00Z",
    "event_id":
        "E15-INVALID-002",
    "event_type":
        "tool_call",
    "trace_id":
        "trace-invalid-002",
    "actor_id":
        "user-test",
    "actor_tenant":
        "tenant-alpha",
    "resource_tenant":
        "tenant-alpha",
    "result":
        "blocked",
    "source":
        "agent",
    "raw_prompt":
        "SYNTHETIC_SHOULD_NEVER_BE_LOGGED",
    "synthetic":
        True,
}

try:
    engine.validate_event(
        invalid_sensitive,
        schema,
    )
except ValueError:
    sensitive_key_rejected = True


# ============================================================
# Alert sensitive-field check
# ============================================================

prohibited = set(
    schema[
        "sensitive_log_policy"
    ][
        "prohibited"
    ]
)

alert_sensitive_key_count = 0

for alert in (
    alerts
    +
    cross_alerts
    +
    negative_alerts
):
    alert_sensitive_key_count += len(
        set(alert)
        &
        prohibited
    )


# ============================================================
# Policy gate
# ============================================================

requirements = policy[
    "release_requirements"
]

checks = {
    "expected_alert_match_rate":
        expected_alert_match_rate
        >=
        requirements[
            "expected_alert_match_rate_min"
        ],

    "precision":
        precision
        >=
        requirements[
            "precision_min"
        ],

    "recall":
        recall
        >=
        requirements[
            "recall_min"
        ],

    "benign_alert_events":
        len(
            benign_alert_events
        )
        <=
        requirements[
            "benign_alert_events_max"
        ],

    "negative_fixture_alerts":
        len(
            negative_alerts
        )
        <=
        requirements[
            "negative_fixture_alerts_max"
        ],

    "cross_event_correlation":
        (
            cross_event_pass
            if
            requirements[
                "cross_event_correlation_required"
            ]
            else
            True
        ),

    "missing_required_field_rejection":
        (
            missing_required_field_rejected
            if
            requirements[
                "missing_required_field_rejection_required"
            ]
            else
            True
        ),

    "sensitive_key_rejection":
        (
            sensitive_key_rejected
            if
            requirements[
                "sensitive_key_rejection_required"
            ]
            else
            True
        ),

    "alert_sensitive_key_count":
        alert_sensitive_key_count
        ==
        0,
}


metrics = {
    "phase": 15,

    "scope":
        "synthetic deterministic detection evaluation",

    "source_fixture_events":
        len(events),

    "expected_security_alerts":
        len(expected),

    "observed_security_alerts":
        len(alerts),

    "true_positives":
        tp,

    "false_positives":
        fp,

    "false_negatives":
        fn,

    "true_negatives":
        tn,

    "precision":
        precision,

    "recall":
        recall,

    "expected_alert_match_rate":
        expected_alert_match_rate,

    "benign_event_count":
        len(benign_events),

    "benign_alert_event_count":
        len(benign_alert_events),

    "negative_fixture_alert_count":
        len(negative_alerts),

    "cross_event_correlation":
        cross_event_pass,

    "missing_required_field_rejected":
        missing_required_field_rejected,

    "sensitive_key_rejected":
        sensitive_key_rejected,

    "alert_sensitive_key_count":
        alert_sensitive_key_count,

    "gate_checks":
        checks,

    "production_effectiveness_claim":
        False,
}

pathlib.Path(
    metrics_path
).write_text(
    json.dumps(
        metrics,
        indent=2,
        sort_keys=True,
    )
    +
    "\n"
)


print(
    f"SOURCE_FIXTURE_EVENTS="
    f"{len(events)}"
)

print(
    f"EXPECTED_ALERTS="
    f"{len(expected)}"
)

print(
    f"OBSERVED_ALERTS="
    f"{len(alerts)}"
)

print(
    f"TRUE_POSITIVES="
    f"{tp}"
)

print(
    f"FALSE_POSITIVES="
    f"{fp}"
)

print(
    f"FALSE_NEGATIVES="
    f"{fn}"
)

print(
    f"TRUE_NEGATIVES="
    f"{tn}"
)

print(
    f"PRECISION="
    f"{precision:.4f}"
)

print(
    f"RECALL="
    f"{recall:.4f}"
)

print(
    "EXPECTED_ALERT_MATCH_RATE="
    f"{expected_alert_match_rate:.4f}"
)

print(
    "NEGATIVE_FIXTURE_ALERTS="
    f"{len(negative_alerts)}"
)

print(
    "CROSS_EVENT_CORRELATION="
    +
    (
        "PASS"
        if cross_event_pass
        else "FAIL"
    )
)

print(
    "MISSING_REQUIRED_FIELD_REJECTION="
    +
    (
        "PASS"
        if missing_required_field_rejected
        else "FAIL"
    )
)

print(
    "SENSITIVE_KEY_REJECTION="
    +
    (
        "PASS"
        if sensitive_key_rejected
        else "FAIL"
    )
)

print(
    "ALERT_SENSITIVE_KEY_CHECK="
    +
    (
        "PASS"
        if
        alert_sensitive_key_count == 0
        else
        "FAIL"
    )
)

for name, value in checks.items():
    print(
        "GATE_"
        +
        name.upper()
        +
        "="
        +
        (
            "PASS"
            if value
            else "FAIL"
        )
    )

if not all(
    checks.values()
):
    print(
        "RESULT=PHASE15_BATCH_B_DETECTION_REGRESSION_FAIL"
    )
    raise SystemExit(1)

print(
    "RESULT=PHASE15_BATCH_B_DETECTION_REGRESSION_PASS"
)
