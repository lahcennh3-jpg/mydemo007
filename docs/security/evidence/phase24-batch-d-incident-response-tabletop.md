# Phase 24 — Current-Cycle Incident-Response Tabletop

Timestamp UTC:

`2026-09-26T17:13:34Z`

TABLETOP_TYPE=SYNTHETIC

REAL_PRODUCTION_INCIDENT=NO

PRODUCTION_DETECTION_VALIDATED=NO

PRODUCTION_CONTAINMENT_VALIDATED=NO

PRODUCTION_RECOVERY_VALIDATED=NO

## Objective

Execute EV23-014 against the current Phase 24 evaluation state rather than
merely inheriting the Phase 23 tabletop.

Each scenario requires:

1. detection/trigger;
2. triage;
3. owner;
4. evidence preservation;
5. containment;
6. root-cause investigation;
7. remediation;
8. recovery;
9. regression/retest;
10. residual-risk decision;
11. communication/release decision.

---

## Scenario IR24-001 — Cross-tenant retrieval

Synthetic condition:

A Tenant Alpha user appears to receive a Tenant Beta resource.

Current evidence:

EV23-003=BLOCKED

EV23-004=BLOCKED

Response:

- preserve actor, tenant, object and authorization-decision identifiers;
- disable or isolate the affected retrieval capability where necessary;
- identify whether authorization occurred before retrieval;
- establish a second-tenant synthetic fixture;
- reproduce cross-tenant access under controlled conditions;
- establish controlled RAG authorization/revocation runtime;
- retest before allowing tenant-isolation or RAG-isolation claims.

Owner:

PROJECT_OWNER

Containment decision:

WITHHOLD_CROSS_TENANT_AND_RAG_SECURITY_CLAIMS

Regression gate:

EV23-003_AND_EV23-004_REQUIRED

Result:

TABLETOP_RESPONSE_DEFINED

---

## Scenario IR24-002 — Indirect prompt injection to privileged tool

Synthetic condition:

Retrieved or user-controlled content attempts to cause unauthorized tool use.

Current evidence:

EV23-005=BLOCKED

EV23-006=BLOCKED

EV23-007=PASS

Response:

- preserve prompt/context/tool-selection metadata;
- distinguish untrusted content from trusted instructions;
- independently enforce tool authorization;
- prevent unauthorized capability execution;
- establish controlled retrieval/model runtime;
- execute direct and indirect injection corpus;
- rerun tool-authority regression after remediation if a failure appears.

Owner:

PROJECT_OWNER

Containment decision:

TOOL_AUTHORITY_CONTROL_EVIDENCE_ACCEPTED

PROMPT_AND_RETRIEVAL_RESILIENCE_CLAIMS_WITHHELD

Regression gate:

EV23-005_AND_EV23-006_REQUIRED

Result:

TABLETOP_RESPONSE_DEFINED

---

## Scenario IR24-003 — MCP or credential boundary failure

Synthetic condition:

A tool/MCP path appears to expose or propagate credentials outside its
intended authorization boundary.

Current evidence:

EV23-008=PASS

EV23-009=PASS

Response:

- preserve credential-flow metadata without preserving raw secrets;
- identify credential owner, audience and capability;
- revoke affected synthetic credential where appropriate;
- validate MCP authorization boundary;
- validate header/credential propagation controls;
- inspect logging/export paths;
- retest redaction and MCP security controls.

Owner:

PROJECT_OWNER

Containment decision:

REVOKE_AFFECTED_CREDENTIAL_AND_DISABLE_AFFECTED_INTEGRATION_IF_NEEDED

Regression gate:

EV23-008_AND_EV23-009

Result:

TABLETOP_RESPONSE_DEFINED

---

## Scenario IR24-004 — Dependency/container provenance change

Synthetic condition:

A security-relevant image or dependency changes unexpectedly.

Current evidence:

EV23-012=PASS

Response:

- freeze current digest/image identity;
- preserve old and new artifact identifiers;
- determine origin of the change;
- prevent automatic upgrade;
- review affected interfaces and controls;
- restore the approved artifact where required;
- rerun selected security regressions;
- update supply-chain evidence.

Owner:

PROJECT_OWNER

Containment decision:

FAIL_CLOSED_ON_UNAPPROVED_RUNTIME_DRIFT

Regression gate:

EV23-012

Result:

TABLETOP_RESPONSE_DEFINED

---

## Scenario IR24-005 — Model/provider behavioral regression

Synthetic condition:

A model/provider change modifies prompt, output or tool-selection behavior.

Current evidence:

EV23-010=BLOCKED

Response:

- freeze provider/model/version identity;
- preserve evaluation corpus and configuration;
- establish controlled model/provider runtime;
- rerun security-relevant model evaluations;
- compare expected and observed behavior;
- identify downstream affected controls;
- roll back or compensate if required;
- retain residual risk until validation completes.

Owner:

PROJECT_OWNER

Containment decision:

WITHHOLD_MODEL_PROVIDER_SECURITY_CLAIMS

Regression gate:

EV23-010_REQUIRED

Result:

TABLETOP_RESPONSE_DEFINED

---

## Completion

TABLETOP_SCENARIOS=5

TABLETOP_SCENARIOS_WITH_OWNER=5

TABLETOP_SCENARIOS_WITH_CONTAINMENT=5

TABLETOP_SCENARIOS_WITH_EVIDENCE_PRESERVATION=5

TABLETOP_SCENARIOS_WITH_RETEST_GATE=5

TABLETOP_SCENARIOS_WITH_RESIDUAL_RISK_DECISION=5

EV23-014=PASS

TABLETOP_RESULT=PASS_FOR_SYNTHETIC_PROCESS_EXERCISE

PRODUCTION_OPERATIONAL_EFFECTIVENESS_CLAIM=NO

ACTION_24.22=PASS_EV23_014_SYNTHETIC_IR_TABLETOP
