import json
import pathlib
import sys

correlation_path = pathlib.Path(sys.argv[1])
detections_path = pathlib.Path(sys.argv[2])
events_path = pathlib.Path(sys.argv[3])

correlation = json.loads(correlation_path.read_text())
detections = json.loads(detections_path.read_text())

events = [
    json.loads(line)
    for line in events_path.read_text().splitlines()
    if line.strip()
]

required = set(
    correlation["required_event_fields"]
)

prohibited = set(
    correlation[
        "sensitive_log_policy"
    ]["prohibited"]
)


def walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_keys(child)


# ------------------------------------------------------------
# Schema
# ------------------------------------------------------------

assert correlation["schema_version"] == "1.0"
assert correlation["phase"] == 15

assert len(
    correlation["security_event_domains"]
) >= 10

assert len(
    correlation["correlation_keys"]
) >= 10


# ------------------------------------------------------------
# Detection requirements
# ------------------------------------------------------------

rules = detections["detections"]

rule_ids = [
    rule["id"]
    for rule in rules
]

assert len(rules) == 9
assert len(rule_ids) == len(set(rule_ids))

expected_rules = {
    f"D15-{number:03d}"
    for number in range(1, 10)
}

assert set(rule_ids) == expected_rules

valid_severity = {
    "low",
    "medium",
    "high",
    "critical",
}

for rule in rules:
    assert rule["severity"] in valid_severity
    assert rule["name"]
    assert rule["condition"]
    assert rule["required_signals"]
    assert rule["triage"]


# ------------------------------------------------------------
# Synthetic events
# ------------------------------------------------------------

assert len(events) >= 12

event_ids = [
    event["event_id"]
    for event in events
]

assert len(event_ids) == len(set(event_ids))

for event in events:
    missing = required - set(event)

    assert not missing, (
        event["event_id"],
        sorted(missing),
    )

    assert event.get("synthetic") is True


# ------------------------------------------------------------
# Every required detection has a synthetic fixture
# ------------------------------------------------------------

fixture_detection_ids = {
    event["expected_detection_id"]
    for event in events
    if "expected_detection_id" in event
}

assert fixture_detection_ids == expected_rules


# ------------------------------------------------------------
# Sensitive-log minimization
# ------------------------------------------------------------

for document in (
    correlation,
    detections,
    events,
):
    keys = set(
        walk_keys(document)
    )

    leaked = keys & prohibited

    assert not leaked, (
        "PROHIBITED_LOG_KEYS_FOUND",
        sorted(leaked),
    )


# ------------------------------------------------------------
# Tenant-correlation sanity checks
# ------------------------------------------------------------

cross_tenant = [
    event
    for event in events
    if event.get(
        "expected_detection_id"
    ) == "D15-001"
]

assert len(cross_tenant) == 1

assert (
    cross_tenant[0]["actor_tenant"]
    !=
    cross_tenant[0]["resource_tenant"]
)

assert (
    cross_tenant[0]["result"]
    == "deny"
)


print(
    f"CORRELATION_SCHEMA_VERSION="
    f"{correlation['schema_version']}"
)

print(
    "SECURITY_EVENT_DOMAINS="
    f"{len(correlation['security_event_domains'])}"
)

print(
    "CORRELATION_KEYS="
    f"{len(correlation['correlation_keys'])}"
)

print(
    f"DETECTION_REQUIREMENTS="
    f"{len(rules)}"
)

print(
    f"SYNTHETIC_EVENTS="
    f"{len(events)}"
)

print(
    "DETECTION_FIXTURE_COVERAGE="
    f"{len(fixture_detection_ids)}/"
    f"{len(expected_rules)}"
)

print(
    "SENSITIVE_LOG_MINIMIZATION=PASS"
)

print(
    "EVENT_SCHEMA_VALIDATION=PASS"
)

print(
    "TENANT_CORRELATION_CHECK=PASS"
)

print(
    "RESULT=PHASE15_BATCH_A_FIXTURES_PASS"
)
