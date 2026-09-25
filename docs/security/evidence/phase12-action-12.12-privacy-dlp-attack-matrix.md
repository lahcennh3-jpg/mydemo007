# Phase 12 Action 12.12 — Consolidated Privacy / DLP Attack Matrix

## Purpose

This matrix consolidates the privacy, sensitive-data and DLP attack surfaces
reviewed during Phase 12 Actions 12.1–12.11.

It distinguishes:

- controls demonstrated by source review or bounded synthetic tests;
- intentional privacy-sensitive data flows;
- retention and deletion limitations;
- residual areas that were not proven by the local assessment.

A PASS means the reviewed control behaved as expected within the tested or
reviewed scope. It does not mean the complete production system is proven free
of privacy defects.

## Matrix

| ID | Boundary / attack case | Expected privacy control | Phase 12 evidence | Result | Interpretation |
|---|---|---|---|---|---|
| P12-01 | Foreign user attempts to read another user's private generated image | Ownership or authorized session must be required | 12.11 synthetic cross-user test | PASS | Foreign user denied |
| P12-02 | Generated-image metadata contains malformed owner identity | Malformed ownership data must fail closed and must not gain access through public-session logic | 12.11 synthetic cross-user test | PASS | Malformed owner denied |
| P12-03 | Foreign user is evaluated against a private UserFile ACL | Only owner and explicitly authorized principals should appear in ACL | 12.11 synthetic cross-user test | PASS | Unrelated user excluded |
| P12-04 | UserFile is explicitly shared through an authorized persona relationship | Intended shared principal should be included without making the file universally public | 12.11 synthetic cross-user test | PASS | Explicit shared user included |
| P12-05 | Multi-tenant retrieval is attempted without required tenant context | Multi-tenant request must fail closed rather than run an unscoped query | 12.11 Vespa tenant-isolation tests | PASS | Missing tenant rejected |
| P12-06 | Tenant Alpha retrieval could potentially include Tenant Beta material | Search filter must scope results to the active tenant | 12.11 Vespa tenant-isolation tests | PASS | Cross-tenant material excluded in tested path |
| P12-07 | Unauthorized adjacent RAG content reaches expanded/final model context | Authorization must be re-applied after retrieval/expansion and unsafe sections removed | 12.6 review + 12.11 RAG authorization tests | PASS | Unauthorized context removed before final model context |
| P12-08 | Identity, preferences or memories are intentionally inserted into model prompt/context | Sensitive personalization must be treated as explicit provider egress rather than invisible internal data | 12.2 + 12.6 | DOCUMENTED_EGRESS | Expected product behavior, privacy-sensitive boundary |
| P12-09 | Incognito or sensitive activity is emitted to external tracing | Incognito external tracing should be suppressed and sensitive trace values masked | 12.7 | PASS | Reviewed tracing controls present |
| P12-10 | Telemetry is disabled by configuration but events continue to leave the system | Telemetry-disable gate must suppress telemetry when disabled | 12.7 | PASS | Disable boundary verified in reviewed path |
| P12-11 | Tool, MCP or custom-provider egress exposes sensitive data through unsafe destination, redirects or headers | Destination validation, redirect restrictions and sensitive-header controls should constrain egress | 12.8 | PASS | Reviewed outbound controls present; external provider behavior not tested |
| P12-12 | User deletes chat, file or account-linked memory but primary data remains reachable | Reviewed primary deletion paths should remove chat/file content and cascade user-linked memory/session records | 12.9 | PASS_WITH_SCOPE_LIMIT | Primary paths reviewed; backups, providers and every derived copy not proven |
| P12-13 | User is deleted but historical usage/accounting records remain | Surviving records should not retain reviewed prompt, message, memory or file content, and retention should be explicit | 12.5 + 12.9 | DOCUMENTED_RETENTION | UserUsage survives with user FK nulled; reviewed fields are usage/accounting metadata |
| P12-14 | Known sensitive synthetic values appear in text that should be scrubbed | Sensitive-value scrubber should redact exact/overlapping values and apply short-value guard | 12.10 functional results | PASS | Targeted redaction behavior verified |
| P12-15 | Non-admin user attempts privileged usage/log export | Export endpoint must enforce administrative authorization | 12.10 | PASS | Reviewed export requires full admin authorization |
| P12-16 | Sensitive data exists in unreviewed paths, backups, provider stores or derived/indexed copies | Assessment must avoid claiming universal DLP or universal deletion without evidence | 12.2–12.10 non-claims | RESIDUAL | General-purpose DLP, provider retention, backup deletion and all derived copies remain outside proven coverage |

## Consolidated observations

### Demonstrated controls

The assessment produced direct evidence for:

- generated-image ownership enforcement;
- UserFile owner/share ACL construction;
- multi-tenant retrieval scoping;
- post-retrieval RAG re-authorization;
- incognito tracing suppression and sensitive-value masking;
- telemetry disable behavior;
- bounded external egress controls;
- primary chat/file/memory deletion mechanisms;
- targeted synthetic-value redaction;
- administrative export authorization.

### Intentional privacy-sensitive flows

The following are not automatically security defects:

- personalization information entering model context;
- authorized model-provider egress;
- authorized MCP/tool egress;
- historical accounting metadata surviving user deletion.

They remain privacy-sensitive boundaries that require purpose,
retention and governance decisions.

### Residual areas

The local Phase 12 evidence does not establish:

- deletion from production backups;
- deletion from external provider stores;
- provider compliance with retention-suppression requests;
- privacy behavior under production-scale telemetry;
- complete isolation of every derived or indexed representation;
- a universal DLP engine covering every application data path.

## Action result

Matrix entries: **16**

Control-pass entries: **11**

Documented intentional/privacy-sensitive boundaries: **3**

Residual/scope-limited entries: **2**

No new confirmed privacy authorization bypass is introduced by this
consolidation action.

**Action 12.12 status: COMPLETE.**
