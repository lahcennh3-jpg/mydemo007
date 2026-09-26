# Phase 23 — 2026 Q3 Threat-Model Delta Refresh

Review timestamp UTC:

`2026-09-26T13:45:24Z`

## Purpose

Refresh threat-model maintenance decisions after the Batch B standards and
upstream-Onyx review without falsely representing upstream drift as a
confirmed vulnerability.

## Protected baseline

Pinned Onyx baseline:

`160f9b143605ca45a85bd387b5bd173840bab15d`

Current upstream release observed during Batch B:

`v4.8.1`

Comparison status:

`ahead`

Total commits reported:

`53`

Changed-file objects returned by the comparison API:

`300`

Security-interest paths selected by bounded keyword triage:

`194`

## Comparison completeness limitation

The changed-file set returned by Batch B must be treated as bounded comparison
metadata.

Because the API returned exactly:

`300`

file objects, the security-interest path count must not be interpreted as
proof that all upstream changed files were enumerated or manually reviewed.

UPSTREAM_DIFF_COMPLETE=NOT_ESTABLISHED

KEYWORD_TRIAGE_COMPLETE_SECURITY_REVIEW=NO

## Threat-delta classes

### TD23-001 — Identity and authentication

Reassess when authentication, session, token or OAuth implementation changes.

Status:

`REASSESS_SELECTED`

### TD23-002 — Authorization and object ownership

Reassess conversation ownership, object authorization, role and permission
enforcement.

Status:

`REASSESS_SELECTED`

### TD23-003 — Tenant isolation

Reassess subject/tenant/resource binding and negative cross-tenant access.

Status:

`REASSESS_SELECTED`

### TD23-004 — RAG and retrieval authorization

Reassess retrieval scope, connector authorization, revocation and stale-access
behavior.

Status:

`REASSESS_SELECTED`

### TD23-005 — Data poisoning and provenance

Reassess ingestion trust, document provenance and poisoned-context behavior.

Status:

`REASSESS_SELECTED`

### TD23-006 — Prompt and instruction boundaries

Reassess direct/indirect prompt injection and instruction-precedence controls.

Status:

`REASSESS_SELECTED`

### TD23-007 — Agent, tool and MCP authority

Reassess tool permissions, MCP identity, excessive agency, confused-deputy
paths and approval boundaries.

Status:

`REASSESS_SELECTED`

### TD23-008 — Sensitive-data and privacy boundaries

Reassess sensitive-data retrieval, disclosure, logging, memory and downstream
tool propagation.

Status:

`REASSESS_SELECTED`

### TD23-009 — Model-security behavior

Reassess behavioral-security controls when model/provider/version changes.

Status:

`REASSESS_SELECTED`

### TD23-010 — Abuse, availability and economic controls

Reassess bounded resources, denial-of-service paths, rate controls and
cost-amplification paths.

Status:

`REASSESS_SELECTED`

### TD23-011 — Software supply chain and deployment

Reassess dependencies, containers, build provenance, externally reachable
surfaces and deployment boundaries.

Status:

`REASSESS_SELECTED`

### TD23-012 — Detection, audit and incident response

Reassess whether relevant abuse and security events are observable,
attributable, retained and actionable.

Status:

`REASSESS_SELECTED`

## Decision

THREAT_DELTA_ITEMS=12

THREAT_MODEL_DELTA_REVIEW=REFRESHED

NEW_CONFIRMED_VULNERABILITY_FROM_MAINTENANCE_METADATA=NO

RUNTIME_VALIDATION_REQUIRED=YES

REGRESSION_EXECUTION_REQUIRED=YES

## Closure rule

A selected threat delta must not be marked mitigated solely because:

- historical evidence exists;
- an upstream release exists;
- a keyword matched a changed path;
- documentation says a control exists.

Closure requires evidence appropriate to the control, such as inspection,
runtime regression, negative authorization testing, evaluation output,
configuration evidence or incident/detection evidence.

## Result

ACTION_23.13=PASS_THREAT_MODEL_DELTA_REFRESH
