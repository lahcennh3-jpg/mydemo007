# Phase 23 — 2026 Q3 Evaluation, Detection and Tabletop Refresh

## Purpose

Convert maintenance deltas into explicit test and operational-security work.

Selection is not execution.

## Evaluation families

### EV23-001 — Authentication negative-path regression

Selected checks:

- unauthenticated route access;
- expired/invalid session behavior;
- token misuse;
- OAuth lifecycle negative paths when applicable.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-002 — Object ownership / BOLA regression

Selected checks:

- conversation ownership;
- object identifier substitution;
- cross-user access;
- server-side ownership enforcement.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-003 — Tenant-isolation regression

Selected checks:

- cross-tenant object access;
- cross-tenant retrieval;
- role/tenant mismatch;
- negative permission tests.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-004 — RAG authorization and revocation

Selected checks:

- unauthorized retrieval;
- stale authorization;
- revoked source access;
- connector permission propagation.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-005 — Retrieval poisoning

Selected checks:

- untrusted retrieved instructions;
- poisoned document context;
- provenance handling;
- trust-boundary enforcement.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-006 — Prompt injection

Selected checks:

- direct prompt injection;
- indirect prompt injection;
- system/instruction hierarchy;
- retrieved-content instruction attacks.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-007 — Agent/tool authorization

Selected checks:

- unauthorized tool selection;
- excessive agency;
- confused-deputy behavior;
- missing approval gates;
- tool argument validation.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-008 — MCP identity and authorization

Selected checks:

- MCP server identity;
- tool permission boundaries;
- credential propagation;
- OAuth/token handling;
- least-privilege behavior.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-009 — Sensitive-data exposure

Selected checks:

- prompt/context leakage;
- retrieval exposure;
- logging exposure;
- tool-output exposure;
- cross-boundary data propagation.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-010 — Model/provider behavior

Selected checks:

- security-control regressions after model change;
- structured-output assumptions;
- refusal/control stability where security relevant;
- tool-selection changes.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-011 — Abuse / availability / economic security

Selected checks:

- bounded concurrency;
- bounded request counts;
- bounded file sizes;
- loop/resource amplification;
- cost-amplification paths.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-012 — Supply-chain / deployment integrity

Selected checks:

- dependency provenance;
- image/container provenance;
- security-relevant configuration delta;
- newly exposed service/interface;
- integrity verification.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-013 — Detection and audit

Selected checks:

- failed authorization visibility;
- suspicious tool/MCP activity;
- abuse/rate signals;
- security-relevant audit attribution;
- evidence retention.

Status:

`SELECTED_NOT_EXECUTED`

### EV23-014 — Incident-response tabletop

Scenario families:

1. cross-tenant retrieval incident;
2. malicious indirect-prompt/tool invocation;
3. credential exposure through connector/MCP path;
4. compromised dependency or deployment artifact;
5. model/provider behavioral regression.

Required tabletop evidence:

- detection;
- triage;
- ownership;
- containment;
- evidence preservation;
- remediation;
- recovery;
- regression;
- residual risk;
- communication decision.

Status:

`SELECTED_NOT_EXECUTED`

## Evaluation integrity rules

The project must preserve:

- test identifier;
- requirement/threat mapping;
- exact baseline;
- input;
- expected result;
- actual result;
- evidence;
- interpretation;
- remediation state;
- regression state.

A historical PASS cannot automatically become a current PASS after a
security-relevant architecture, policy, dependency, model or release change.

## Current state

EVALUATION_FAMILIES_SELECTED=14

EVALUATION_EXECUTION_COMPLETE=NO

DETECTION_REFRESH_SELECTED=YES

INCIDENT_TABLETOP_SELECTED=YES

RUNTIME_REGRESSION_REQUIRED=YES

## Result

ACTION_23.14=PASS_EVALUATION_DETECTION_TABLETOP_REFRESH
