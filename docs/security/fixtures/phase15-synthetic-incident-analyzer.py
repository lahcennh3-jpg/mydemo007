import hashlib
import json
import pathlib
import sys
from collections import Counter


(
    events_path,
    alerts_path,
    correlation_path,
    requirements_path,
    policy_path,
    engine_path,
    timeline_path,
    investigation_path,
    evidence_index_path,
) = sys.argv[1:]


def jsonl(path):
    return [
        json.loads(line)
        for line
        in pathlib.Path(path).read_text().splitlines()
        if line.strip()
    ]


def sha256(path):
    h = hashlib.sha256()

    with pathlib.Path(path).open("rb") as f:
        while True:
            block = f.read(65536)

            if not block:
                break

            h.update(block)

    return h.hexdigest()


events = jsonl(events_path)
alerts = jsonl(alerts_path)

assert len(events) == 7
assert len(alerts) == 6


incident_ids = {
    event.get("incident_id")
    for event in events
}

assert incident_ids == {
    "INC-P15-001"
}


# ============================================================
# Expected detections
# ============================================================

expected_detection_ids = {
    "D15-001",
    "D15-003",
    "D15-004",
    "D15-005",
    "D15-007",
    "D15-009",
}

actual_detection_ids = {
    alert["detection_id"]
    for alert in alerts
}

assert (
    actual_detection_ids
    ==
    expected_detection_ids
)


# ============================================================
# Cross-event prompt/tool correlation
# ============================================================

tool_alerts = [
    alert
    for alert in alerts
    if alert["detection_id"]
    ==
    "D15-003"
]

assert len(tool_alerts) == 1

assert {
    "INC15-E001",
    "INC15-E002",
}.issubset(
    set(
        tool_alerts[0][
            "correlated_event_ids"
        ]
    )
)


# ============================================================
# Sensitive-log validation
# ============================================================

schema = json.loads(
    pathlib.Path(
        correlation_path
    ).read_text()
)

prohibited = set(
    schema[
        "sensitive_log_policy"
    ][
        "prohibited"
    ]
)

for record in events + alerts:
    leaked = (
        set(record)
        &
        prohibited
    )

    assert not leaked, (
        "PROHIBITED_KEY",
        sorted(leaked),
    )


# ============================================================
# Timeline
# ============================================================

events_sorted = sorted(
    events,
    key=lambda item: item["timestamp"],
)

alerts_by_event = {}

for alert in alerts:
    alerts_by_event.setdefault(
        alert["event_id"],
        [],
    ).append(
        alert["detection_id"]
    )


timeline_lines = [
    "# Phase 15 — Synthetic Incident Timeline",
    "",
    "Incident: `INC-P15-001`",
    "",
    "This is a synthetic local security exercise.",
    "",
    "| Timestamp | Event | Type | Result | Detection |",
    "| --- | --- | --- | --- | --- |",
]

for event in events_sorted:
    detection_text = ", ".join(
        sorted(
            alerts_by_event.get(
                event["event_id"],
                [],
            )
        )
    )

    if not detection_text:
        detection_text = (
            "correlation signal / no direct alert"
        )

    timeline_lines.append(
        "| "
        + event["timestamp"]
        + " | "
        + event["event_id"]
        + " | "
        + event["event_type"]
        + " | "
        + event["result"]
        + " | "
        + detection_text
        + " |"
    )

pathlib.Path(
    timeline_path
).write_text(
    "\n".join(
        timeline_lines
    )
    +
    "\n"
)


# ============================================================
# Scope
# ============================================================

actors = sorted({
    event["actor_id"]
    for event in events
})

actor_tenants = sorted({
    event["actor_tenant"]
    for event in events
})

resource_tenants = sorted({
    event["resource_tenant"]
    for event in events
})

traces = sorted({
    event["trace_id"]
    for event in events
})

sources = sorted({
    event["source"]
    for event in events
})

severity_counts = Counter(
    alert["severity"]
    for alert in alerts
)


investigation = f"""# Phase 15 — Synthetic Incident Investigation Report

## Incident

`INC-P15-001`

## Classification

Synthetic local AI application security incident exercise.

No production compromise is claimed.

## Initial triage

Observed correlated security signals include:

- confirmed synthetic prompt-injection signal;
- attempted tool invocation following that signal;
- cross-tenant authorization attempt;
- cross-tenant retrieval/provenance anomaly;
- unapproved prompt-policy configuration change;
- unapproved runtime destination;
- excessive resource activity.

## Detection result

Events reviewed: **{len(events)}**

Alerts generated: **{len(alerts)}**

Unique detection IDs: **{len(actual_detection_ids)}**

Expected detection coverage: **6 / 6**

High-severity alerts: **{severity_counts.get("high", 0)}**

Medium-severity alerts: **{severity_counts.get("medium", 0)}**

## Scope

Actors:

{chr(10).join("- `" + x + "`" for x in actors)}

Actor tenants:

{chr(10).join("- `" + x + "`" for x in actor_tenants)}

Resource tenants:

{chr(10).join("- `" + x + "`" for x in resource_tenants)}

Trace identifiers:

{chr(10).join("- `" + x + "`" for x in traces)}

Event sources:

{chr(10).join("- `" + x + "`" for x in sources)}

## Impact assessment

Because this is a synthetic exercise:

- real users affected: 0;
- real credentials exposed: 0;
- real customer data exposed: 0;
- production systems affected: 0;
- external destination contacted: 0.

Security controls blocked or denied the modeled actions.

This does not prove equivalent production detection or prevention performance.

## Evidence-preservation approach

Evidence is preserved as immutable repository artifacts plus SHA-256 hashes.

Raw prompts, responses and document contents are deliberately excluded.

## Investigation result

`SYNTHETIC_INCIDENT_SCOPED_AND_INVESTIGATED`
"""

pathlib.Path(
    investigation_path
).write_text(
    investigation
)


# ============================================================
# Evidence index
# ============================================================

evidence_paths = [
    events_path,
    alerts_path,
    correlation_path,
    requirements_path,
    policy_path,
    engine_path,
]

evidence_index = {
    "incident_id":
        "INC-P15-001",

    "synthetic":
        True,

    "evidence_integrity_algorithm":
        "sha256",

    "artifacts": [
        {
            "path": path,
            "sha256": sha256(path),
        }
        for path
        in evidence_paths
    ],

    "event_count":
        len(events),

    "alert_count":
        len(alerts),

    "detection_ids":
        sorted(
            actual_detection_ids
        ),

    "raw_sensitive_content_preserved":
        False,

    "production_evidence":
        False,
}

pathlib.Path(
    evidence_index_path
).write_text(
    json.dumps(
        evidence_index,
        indent=2,
        sort_keys=True,
    )
    +
    "\n"
)


print(
    "INCIDENT_ID=INC-P15-001"
)

print(
    f"INCIDENT_EVENTS={len(events)}"
)

print(
    f"INCIDENT_ALERTS={len(alerts)}"
)

print(
    "EXPECTED_DETECTION_COVERAGE="
    f"{len(actual_detection_ids)}/"
    f"{len(expected_detection_ids)}"
)

print(
    f"ACTORS_SCOPED={len(actors)}"
)

print(
    f"TRACES_SCOPED={len(traces)}"
)

print(
    "CROSS_EVENT_CHAIN=PASS"
)

print(
    "SENSITIVE_LOG_CHECK=PASS"
)

print(
    "FORENSIC_HASHING=PASS"
)

print(
    "TIMELINE_GENERATION=PASS"
)

print(
    "INVESTIGATION_REPORT=PASS"
)

print(
    "RESULT=PHASE15_ACTION_15_11_PASS"
)
