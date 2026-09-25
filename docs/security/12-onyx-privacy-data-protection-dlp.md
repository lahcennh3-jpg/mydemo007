# Phase 12 — Onyx Privacy / Data Protection / DLP

## Status

**Phase 12: IN PROGRESS**

## Parent

Phase 11 final SHA:

`7dc4350614b432edfc0d871e202704b3cf2d4c70`

## Objective

Assess privacy and sensitive-data handling across identity, chat, files,
retrieval, memory, connectors, tools, providers, telemetry, retention,
deletion, export and DLP boundaries.

## Core principles

- synthetic data only;
- least necessary collection;
- explicit ownership;
- explicit egress;
- sensitive-data minimization;
- bounded retention;
- reliable deletion;
- redaction before unsafe boundaries;
- tenant/user isolation;
- evidence-based privacy claims.

## Action 12.1 — Initialization and privacy charter

Phase 12 was created directly from the completed Phase 11 SHA.

The privacy scope, synthetic-data rules, evidence model, data classes, stop
conditions and completion criteria were fixed before technical privacy testing.

**Action 12.1 status: COMPLETE.**

## Action 12.2 — Sensitive-data architecture and data-flow inventory

Action 12.2 mapped identity, conversation, retrieval, memory, files,
credentials, OAuth, provider, telemetry and usage-data flows.

Privacy review will treat telemetry, model providers and derived/indexed copies
as independent data boundaries rather than assuming the primary database is
the only privacy-relevant store.

**Action 12.2 status: COMPLETE.**

## Action 12.3 — Data classification, ownership and tenant boundaries

Action 12.3 classified identity, content, source, credential and operational
data and traced the primary ownership boundaries.

Chat, memory and credential paths contain explicit user-scoping controls.

Low-level user-file ID helpers are not treated as authorization APIs; their
externally reachable consumers remain candidates for direct negative testing.

No cross-user privacy bypass was confirmed by this action.

**Action 12.3 status: COMPLETE.**

## Action 12.4 — Collection, minimization and purpose boundaries

Action 12.4 verified multiple content-minimization properties in incognito
operation, including bounded ephemeral context, provider retention-suppression
requests, filename/title minimization and image removal.

Provider compliance with requested retention settings is not independently
claimed.

No collection-overreach finding was confirmed by this action.

**Action 12.4 status: COMPLETE.**

## Action 12.5 — Sensitive storage, secrets and PII inventory

Action 12.5 inventoried user/account data, chat content, persistent memory,
file/blob representations, connector credentials, OAuth data and telemetry
identifiers.

A deliberate retention exception was recorded for later testing: historical
user-usage rows survive user deletion with their user foreign key nulled.

This is not yet classified as a privacy defect; Action 12.9 will verify the
actual retained fields and deletion semantics.

**Action 12.5 status: COMPLETE.**

## Action 12.6 — Prompt, context and RAG privacy leakage

Action 12.6 verified user ACL, document-set authorization, tenant filtering and
post-query censoring boundaries before retrieved content reaches model context.

Prompt construction intentionally exposes personalization data such as identity,
preferences and memories to the model context when configured.

That is recorded as a privacy-sensitive provider-egress surface rather than an
unauthorized disclosure finding.

**Action 12.6 status: COMPLETE.**

## Action 12.7 — Logs, traces, telemetry and error disclosure

Action 12.7 verified incognito external-trace suppression, sensitive trace
masking and the telemetry disable gate.

External tracing, telemetry event payloads and persisted background error
messages remain explicit privacy-sensitive secondary-data boundaries.

No unauthorized observability disclosure was confirmed by this static action.

**Action 12.7 status: COMPLETE.**

## Action 12.8 — Connector, tool, MCP and provider egress

Action 12.8 mapped external model, custom-tool and MCP boundaries and verified
outbound URL validation, redirect suppression, MCP header filtering, SSRF-aware
transport construction and bounded MCP call timing.

All verification was offline; no real external provider or tool endpoint was
contacted.

**Action 12.8 status: COMPLETE.**

## Action 12.9 — Conversation, file and memory retention / deletion

Action 12.9 verified chat hard-delete paths, file-store deletion primitives and
user-cascade behavior for memory and chat sessions.

The Action 12.5 retention exception was narrowed: UserUsage intentionally
survives user deletion with its direct user foreign key nulled, while the
reviewed schema contains usage/accounting fields rather than prompt, message,
memory or file content.

This evidence does not claim deletion from production backups, external
provider stores or every derived representation.

**Action 12.9 status: COMPLETE.**

## Action 12.10 — DLP, redaction, export and download controls

Action 12.10 functionally verified synthetic-value redaction and reviewed
administrative log and usage export authorization.

The evidence supports targeted redaction and masking controls, not a claim that
every Onyx data path is protected by a general-purpose DLP engine.

No reviewed export-authorization or redaction bypass was confirmed.

**Action 12.10 status: COMPLETE.**

## Action 12.11 — Cross-user and cross-tenant privacy negative tests

Action 12.11 executed bounded synthetic privacy-isolation negative tests
covering generated-image ownership, malformed ownership metadata, private
and explicitly shared user-file ACL behavior, multi-tenant Vespa filtering,
and post-retrieval RAG authorization.

A foreign user was denied access to a private generated image. Malformed
generated-image ownership metadata failed closed. A private user file excluded
an unrelated synthetic user, while an explicit share added the intended user
to the ACL.

The Vespa isolation tests verified missing-tenant fail-closed behavior,
tenant filtering and the single-tenant case. The RAG authorization tests
verified removal of unauthorized adjacent content, removal of a section when
its authorized center is removed, re-censoring before final model context,
and absence of citations when no safe section remains.

Execution used a source-matched Docker test runtime with networking disabled
and synthetic identities only.

This action does not claim complete production authorization coverage,
provider-side privacy guarantees, backup deletion guarantees, or complete
isolation of every derived representation.

**Action 12.11 status: COMPLETE.**

## Action 12.12 — Consolidated privacy and DLP attack matrix

Action 12.12 consolidated the Phase 12 privacy assessment into a 16-case
attack/control matrix spanning cross-user access, tenant isolation, RAG
authorization, personalization/provider egress, observability, external tools,
retention/deletion, redaction and administrative export.

The matrix separates demonstrated controls from intentional privacy-sensitive
flows and residual areas where the local assessment does not support a complete
production guarantee.

No new privacy authorization bypass was confirmed by the consolidation action.
The remaining scope limitations include provider retention, production backups,
all derived/indexed copies and universal DLP coverage.

**Action 12.12 status: COMPLETE.**

## Action 12.13 — Bounded synthetic privacy runtime

Action 12.13 executed the consolidated Phase 12 regression set inside the
source-matched Docker test runtime with Docker networking disabled.

Ten suites containing 46 tests covered ownership, minimization, prompt/RAG
privacy, observability, external egress, retention/deletion, DLP/redaction,
cross-user access, tenant isolation and post-retrieval RAG authorization.

All 46 tests passed within the bounded runtime. No real credentials, personal
data, provider calls, MCP endpoints or external network services were used.

The runtime evidence remains local/unit-level evidence and does not establish
production backup deletion, external-provider retention compliance,
production-scale observability behavior or universal DLP coverage.

**Action 12.13 status: COMPLETE.**

## Action 12.14 — Findings, regression and framework mapping

Action 12.14 consolidated Phase 12 findings, privacy-sensitive boundaries,
regression evidence, residual risks, responsibility boundaries and an
engineering framework crosswalk.

The Action 12.13 regression evidence establishes a bounded 46/46-test local
privacy regression pass with Docker networking disabled.

No new privacy authorization bypass was confirmed in the reviewed Phase 12
scope. Explicit residuals remain for production backups, external-provider
retention/deletion, every derived/indexed representation, production
observability behavior and universal DLP coverage.

The framework mapping is an engineering crosswalk rather than a certification
or legal/compliance claim.

**Action 12.14 status: COMPLETE.**
