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

## Action 15.10 — Synthetic security incident exercise

Synthetic incident:

`INC-P15-001`

The incident contains seven security-relevant events and produced six
deterministic alerts.

No production system or external destination was contacted.

Evidence:

`docs/security/fixtures/phase15-synthetic-incident-events-v1.jsonl`

`docs/security/evidence/phase15-action-15.10-incident-alerts.jsonl`

**Action 15.10 status: COMPLETE.**

## Action 15.11 — Triage, timeline, scope and forensic evidence

The synthetic incident was reconstructed and scoped using normalized events,
trace identifiers, tenant identifiers and generated alerts.

Validated:

- expected detections: 6 / 6;
- cross-event correlation: PASS;
- sensitive-log check: PASS;
- SHA-256 forensic evidence indexing: PASS;
- timeline reconstruction: PASS.

Evidence:

`docs/security/evidence/phase15-action-15.11-incident-timeline.md`

`docs/security/evidence/phase15-action-15.11-investigation-report.md`

`docs/security/evidence/phase15-action-15.11-forensic-evidence-index.json`

**Action 15.11 status: COMPLETE.**

## Action 15.12 — Containment, eradication and recovery

A security-response runbook was produced covering:

- evidence preservation;
- identity containment;
- tenant authorization containment;
- agent/tool/MCP containment;
- retrieval containment;
- configuration rollback;
- eradication criteria;
- recovery criteria;
- rollback triggers.

No real containment action was executed.

Runbook:

`docs/security/evidence/phase15-action-15.12-containment-eradication-recovery-runbook.md`

**Action 15.12 status: COMPLETE.**

## Action 15.13 — Notification decision and lessons learned

The synthetic exercise notification decision was documented.

Because no real users, credentials, customer data or production systems were
affected, external incident notification is not applicable to this synthetic
exercise.

Real-world legal and contractual notification decisions remain outside the
exercise and require appropriate organizational review.

Evidence:

`docs/security/evidence/phase15-action-15.13-notification-decision.md`

`docs/security/evidence/phase15-action-15.13-lessons-learned.md`

**Action 15.13 status: COMPLETE.**

## Action 15.14 — Preventive regression and incident-response gate

The complete synthetic incident was replayed through the local detection
engine.

Expected incident detections:

- D15-001;
- D15-003;
- D15-004;
- D15-005;
- D15-007;
- D15-009.

Result:

**6 / 6 PASS**

Incident-response gate:

`PHASE15_INCIDENT_RESPONSE_GATE_PASS`

Evidence:

`docs/security/evidence/phase15-action-15.14-preventive-regression.txt`

`docs/security/evidence/phase15-action-15.14-final-ir-gate.txt`

**Action 15.14 status: COMPLETE.**

## Action 15.15 — Evidence, residual risk and phase closeout

Tooling status and deployment limitations were documented explicitly.

The phase verifies the local synthetic security-observability, detection,
forensics and incident-response workflow.

It does not claim production detection or incident-response assurance.

Closeout:

`docs/security/evidence/phase15-final-closeout.md`

Tool status:

`docs/security/evidence/phase15-action-15.15-tooling-status.md`

Final classification:

`PHASE_15_COMPLETE_WITH_DOCUMENTED_RESIDUAL_RISKS`

**Action 15.15 status: COMPLETE.**

## Phase 15 final status

Actions complete:

**15 / 15**

Progress:

**100%**

Result:

`PHASE_15_COMPLETE_WITH_DOCUMENTED_RESIDUAL_RISKS`
