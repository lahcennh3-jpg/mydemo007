# Phase 15 — Synthetic Incident Investigation Report

## Incident

`INC-P15-001`

## Classification

Synthetic local AI application security incident exercise.

No production compromise is claimed.

## Initial triage

Observed correlated security signals include:

- confirmed synthetic prompt-injection signal;
- attempted tool invocation following that signal;
- cross-tenant authorization attempt;
- cross-tenant retrieval/provenance anomaly;
- unapproved prompt-policy configuration change;
- unapproved runtime destination;
- excessive resource activity.

## Detection result

Events reviewed: **7**

Alerts generated: **6**

Unique detection IDs: **6**

Expected detection coverage: **6 / 6**

High-severity alerts: **4**

Medium-severity alerts: **2**

## Scope

Actors:

- `agent-inc15-001`
- `synthetic-admin`
- `user-alice`

Actor tenants:

- `system`
- `tenant-alpha`

Resource tenants:

- `system`
- `tenant-alpha`
- `tenant-beta`

Trace identifiers:

- `trace-inc15-agent`
- `trace-inc15-config`
- `trace-inc15-resource`
- `trace-inc15-retrieval`
- `trace-inc15-runtime`
- `trace-inc15-tenant`

Event sources:

- `agent`
- `api`
- `prompt-security`
- `quota`
- `release`
- `retrieval`
- `runtime`

## Impact assessment

Because this is a synthetic exercise:

- real users affected: 0;
- real credentials exposed: 0;
- real customer data exposed: 0;
- production systems affected: 0;
- external destination contacted: 0.

Security controls blocked or denied the modeled actions.

This does not prove equivalent production detection or prevention performance.

## Evidence-preservation approach

Evidence is preserved as immutable repository artifacts plus SHA-256 hashes.

Raw prompts, responses and document contents are deliberately excluded.

## Investigation result

`SYNTHETIC_INCIDENT_SCOPED_AND_INVESTIGATED`
