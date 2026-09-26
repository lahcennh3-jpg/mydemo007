# Phase 23 — 2026 Q3 Security Delta Triage

Review timestamp UTC:

`2026-09-26T13:41:31Z`

## Inputs

- current NIST AI RMF source;
- NIST AI 600-1 context;
- NIST SP 800-218A;
- OWASP LLM Top 10 2026;
- OWASP Agentic Applications Top 10 2026;
- OWASP Agent Control Standard;
- OWASP ASVS;
- current Onyx upstream release metadata;
- Onyx baseline-to-current comparison metadata.

## Delta classification

### D23-B-001 — Framework freshness

Status:

`REVIEW_REQUIRED_WHEN_MAPPING_DIFF_EXISTS`

Response:

- preserve the existing mappings;
- identify revised/new framework requirements;
- update only mappings supported by evidence;
- do not rewrite historical findings retroactively.

### D23-B-002 — Onyx architecture and implementation drift

Status:

`TECHNICAL_REASSESSMENT_REQUIRED`

Reason:

The maintained project baseline and current upstream release are not assumed
to be equivalent.

Response:

- inspect security-interest changes;
- select relevant regression tests;
- reassess threat boundaries affected by upstream changes;
- preserve the original project baseline for reproducibility.

### D23-B-003 — Authentication / authorization / OAuth

Status:

`CONDITIONAL_REGRESSION_REQUIRED`

Regression families when affected:

- unauthenticated access;
- broken object authorization;
- conversation ownership;
- role/permission enforcement;
- tenant isolation;
- OAuth/token lifecycle;
- negative authorization paths.

### D23-B-004 — RAG / retrieval / connector changes

Status:

`CONDITIONAL_REGRESSION_REQUIRED`

Regression families when affected:

- unauthorized retrieval;
- cross-tenant retrieval;
- connector authorization;
- stale/revoked access;
- poisoning;
- sensitive-data exposure.

### D23-B-005 — Agent / tool / MCP changes

Status:

`CONDITIONAL_REGRESSION_REQUIRED`

Regression families when affected:

- tool authorization;
- confused-deputy paths;
- tool argument validation;
- indirect prompt injection;
- approval boundaries;
- excessive agency;
- credential propagation;
- MCP identity and authorization;
- auditability and rollback.

### D23-B-006 — Model / prompt behavior changes

Status:

`CONDITIONAL_EVALUATION_REFRESH_REQUIRED`

Regression families when affected:

- instruction hierarchy;
- prompt injection;
- unsafe information flow;
- sensitive-data handling;
- output validation;
- tool-selection behavior.

### D23-B-007 — Dependency / deployment changes

Status:

`CONDITIONAL_SUPPLY_CHAIN_REVIEW_REQUIRED`

Review when affected:

- dependency provenance;
- vulnerability advisories;
- container/image provenance;
- deployment boundary changes;
- new externally reachable services;
- integrity validation.

## Current decision

STANDARDS_REFRESH_COMPLETED=YES

ONYX_UPSTREAM_REFRESH_COMPLETED=YES

PINNED_ONYX_BASELINE_CHANGED=NO

AUTOMATIC_UPGRADE=NO

AUTOMATIC_SECURITY_FINDING=NO

REGRESSION_SELECTION_REQUIRED=YES

THREAT_MODEL_DELTA_REVIEW_REQUIRED=YES

## Important limitation

The current upstream comparison is maintenance-selection evidence.

It must not be represented as:

- a complete new penetration test;
- proof that current upstream Onyx is secure;
- proof that the old baseline is insecure;
- proof that every changed file was manually reviewed.

## Result

ACTION_23.9=PASS_SECURITY_DELTA_TRIAGE
