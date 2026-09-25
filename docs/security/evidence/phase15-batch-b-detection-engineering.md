# Phase 15 — Accelerated Batch B Detection Engineering

## Scope

Actions 15.5 through 15.9.

## 15.5 — Deterministic local detection engine

Implemented executable local detection logic for:

- cross-tenant authorization attempts;
- privilege/service-account anomalies;
- prompt-injection-to-tool-call correlation;
- unexpected runtime destinations;
- retrieval provenance anomalies;
- DLP and telemetry gaps;
- unapproved security-configuration changes;
- security-behavior drift;
- excessive resource/economic activity.

The engine consumes the normalized Phase 15 security-event schema.

## 15.6 — Cross-event correlation

A prompt-security event and subsequent tool-call event were correlated using a
shared trace identifier.

The tool-call alert preserves event identifiers rather than prompt content.

## 15.7 — Detection-quality evaluation

Deterministic synthetic fixture result:

- expected alerts: 9;
- observed alerts: 9;
- true positives: 9;
- false positives: 0;
- false negatives: 0;
- true negatives: 3;
- precision: 1.0;
- recall: 1.0.

These measurements apply only to the controlled synthetic fixture set.

They are not estimates of production detection effectiveness.

## 15.8 — Telemetry and sensitive-log negative testing

Verified:

- benign fixture set produces zero alerts;
- missing mandatory telemetry fields are rejected;
- prohibited sensitive log keys are rejected;
- generated alerts contain no prohibited content fields.

## 15.9 — Regression gate

The deterministic Batch B release gate passed.

The gate validates detection logic and synthetic evidence only.

It does not claim deployment to a production SIEM or observability platform.

## Safety

- synthetic data only;
- network-disabled execution;
- real credentials: 0;
- real user data: 0;
- production telemetry: 0;
- remote telemetry export: 0.

## Result

`PHASE_15_BATCH_B_PASS`
