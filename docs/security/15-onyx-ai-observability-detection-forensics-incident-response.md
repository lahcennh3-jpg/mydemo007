# Phase 15 — AI Observability, Detection Engineering, Forensics, and Incident Response

## Objective

Build a security-observability and incident-response capability for the local
Onyx security lab.

The phase connects preventive controls from earlier phases to:

- security telemetry;
- event correlation;
- detections;
- investigation;
- forensic evidence;
- containment;
- recovery;
- preventive regression.

## Safety boundary

Allowed:

- local source inspection;
- synthetic security events;
- deterministic detection logic;
- network-disabled Docker execution;
- synthetic incident reconstruction;
- local evidence and runbooks.

Prohibited:

- production telemetry;
- real customer data;
- real credentials;
- remote SIEM export;
- remote Langfuse export;
- real incident-response actions;
- destructive containment;
- unrestricted network capture;
- raw prompt or response logging.

## Logging principle

Security telemetry must be useful for detection and investigation while
minimizing sensitive content.

Prefer identifiers, hashes, classifications, decisions, counters and versions.

Do not log complete:

- prompts;
- model responses;
- retrieved documents;
- credentials;
- API keys;
- access tokens;
- cookies;
- personal data.

## Phase architecture

Security event
→ normalized event schema
→ correlation identifiers
→ detection rule
→ alert
→ triage
→ investigation
→ containment decision
→ recovery
→ preventive regression.

## Action 15.1 — Scope and immutable handoff

Phase 14 is treated as an immutable parent checkpoint.

Phase 15 operates only on local source, synthetic events and bounded isolated
runtime validation.

**Action 15.1 status: COMPLETE.**

## Action 15.2 — Security telemetry inventory

Pending Batch A generation.

## Action 15.3 — Correlation and sensitive-log model

Pending Batch A generation.

## Action 15.4 — Detection requirements and synthetic fixtures

Pending Batch A generation.

## Action 15.2 — Security telemetry inventory

A bounded source-level telemetry inventory was generated covering:

- authentication and authorization;
- tenant identity;
- connectors and ingestion;
- retrieval and provenance;
- model / embedding / reranker / prompt configuration;
- agents, actions, tools and MCP;
- DLP and sensitive-data controls;
- quotas, tokens, cost, timeout and queues;
- administration and release events;
- process, filesystem, container and network surfaces.

Inventory:

`docs/security/evidence/phase15-batch-a-security-telemetry-inventory.txt`

Inventory lines:

**2308**

A source match represents a candidate telemetry location, not proof that a
production-quality security event already exists.

**Action 15.2 status: COMPLETE.**

## Action 15.3 — Correlation and sensitive-log model

A normalized security-event correlation model was created.

It defines correlation across:

- requests;
- sessions;
- conversations;
- tenants;
- connectors;
- retrieval operations;
- model and policy versions;
- agent runs;
- tool calls;
- MCP servers;
- approvals;
- deployments.

Sensitive-log minimization explicitly prohibits raw prompts, raw responses,
retrieved document content, credentials, tokens and cookies.

Model:

`docs/security/fixtures/phase15-security-event-correlation-model-v1.json`

**Action 15.3 status: COMPLETE.**

## Action 15.4 — Detection requirements and synthetic fixtures

Nine security detection requirements were defined:

1. cross-tenant access attempts;
2. privilege and service-account anomalies;
3. prompt-injection-to-tool-call correlation;
4. unexpected runtime or tool destinations;
5. retrieval provenance anomalies;
6. DLP or telemetry gaps;
7. unapproved model/prompt/policy/configuration changes;
8. security-behavior drift;
9. excessive recursion, tokens, concurrency, tool calls or cost.

Every detection requirement has at least one synthetic event fixture.

No production events were used.

Detection requirements:

`docs/security/fixtures/phase15-detection-requirements-v1.json`

Synthetic fixtures:

`docs/security/fixtures/phase15-synthetic-security-events-v1.jsonl`

Validation:

`docs/security/evidence/phase15-batch-a-fixture-validation.txt`

**Action 15.4 status: COMPLETE.**

## Batch A status

Actions complete:

**15.1–15.4**

Phase progress:

**4 / 15**

Next:

**Accelerated Batch B — Actions 15.5–15.9**

## Action 15.5 — Deterministic local detection engine

A local detection engine was implemented for all nine Phase 15 detection
requirements.

Evidence:

`docs/security/evidence/phase15-batch-b-alerts.jsonl`

Policy:

`docs/security/fixtures/phase15-detection-policy-v1.json`

Engine:

`docs/security/fixtures/phase15-local-detection-engine.py`

**Action 15.5 status: COMPLETE.**

## Action 15.6 — Cross-event security correlation

Prompt-security and tool-call events were correlated by trace identifier.

The test verifies a prompt-injection security signal can be connected to a
later tool invocation without storing raw prompt text.

Evidence:

`docs/security/evidence/phase15-batch-b-cross-event-alerts.jsonl`

**Action 15.6 status: COMPLETE.**

## Action 15.7 — Detection quality evaluation

Synthetic deterministic evaluation produced:

- expected alerts: 9;
- observed alerts: 9;
- true positives: 9;
- false positives: 0;
- false negatives: 0;
- true negatives: 3;
- precision: 1.0;
- recall: 1.0.

These values apply only to the controlled synthetic test corpus.

Production detection effectiveness remains unmeasured.

Metrics:

`docs/security/evidence/phase15-batch-b-detection-metrics.json`

**Action 15.7 status: COMPLETE.**

## Action 15.8 — Telemetry-gap and sensitive-log negative testing

Validated:

- benign events generate zero alerts;
- missing required telemetry fields are rejected;
- prohibited sensitive event keys are rejected;
- alerts do not contain prohibited log fields.

Evidence:

`docs/security/evidence/phase15-batch-b-detection-results.txt`

**Action 15.8 status: COMPLETE.**

## Action 15.9 — Deterministic detection regression gate

The Batch B release gate requires all deterministic detection, correlation,
negative-test and sensitive-log controls to pass.

Result:

`PHASE15_BATCH_B_RELEASE_GATE_PASS`

Evidence:

`docs/security/evidence/phase15-batch-b-regression-gate.txt`

**Action 15.9 status: COMPLETE.**

## Batch B status

Actions complete:

**15.5–15.9**

Cumulative Phase 15 progress:

**9 / 15**

Next:

**Accelerated Batch C — Actions 15.10–15.15**
