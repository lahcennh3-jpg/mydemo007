# Phase 14 — Onyx Continuous LLM, RAG, Agent and MCP Red Team

## Objective

Build a repeatable, evidence-driven continuous AI security evaluation and
release-gating capability around the approved synthetic Onyx laboratory.

## Immutable parent

Phase 13 — Abuse / Misuse / Availability / Economic Security.

Parent:

`73a29e9eca13a4e475cb0f019c83fab231023589`

## Safety boundary

- synthetic identities, prompts, documents, credentials and incidents only;
- no production systems;
- no real users or user data;
- no real credentials;
- no paid external model or AI API;
- no uncontrolled remote attack generation;
- no destructive denial-of-service testing;
- maximum 100 requests per bounded case;
- maximum 10 concurrent operations;
- maximum 60 seconds per bounded runtime case;
- unexpected network access is a stop condition;
- discovery of real data or credentials is a stop condition;
- scope uncertainty is a stop condition.

## Attack domains

- direct prompt injection;
- indirect prompt injection;
- retrieval poisoning;
- knowledge-base poisoning;
- cross-tenant access;
- sensitive-data exposure;
- unauthorized actions;
- MCP and tool abuse;
- tool-description poisoning;
- tool shadowing;
- structured-output failures;
- protected-context disclosure;
- memory injection;
- citation and provenance manipulation;
- revoked/deleted-content retrieval;
- refusal failure;
- over-refusal;
- multi-turn attacks;
- multi-agent delegation attacks;
- recursion and tool-loop behavior;
- security-control regression;
- evaluator integrity;
- evaluation-data security;
- continuous release gating.

## Measurement principle

Deterministic application controls and model-dependent behavior are evaluated
separately.

Source review alone never converts a case into PASS.

Untested cases remain NOT_VERIFIED.

**Action 14.1 status: COMPLETE.**

## Action 14.2 — Existing security-test inventory

Prior authorization, tenant-isolation, RAG, agent/tool, privacy/DLP and
abuse-security evidence was inventoried.

Evidence:

`docs/security/evidence/phase14-batch-a-existing-security-test-inventory.txt`

Inventory lines:

539

Previously validated deterministic controls can therefore be reused as
continuous regression oracles.

This does not imply that model-dependent attack cases have been executed.

**Action 14.2 status: COMPLETE.**

## Action 14.3 — Versioned synthetic attack dataset

Dataset:

`docs/security/fixtures/phase14-synthetic-red-team-dataset-v1.jsonl`

Version:

v1

Cases:

24

Every new attack case starts as:

`NOT_VERIFIED`

Cases are promoted only when appropriate evidence exists.

**Action 14.3 status: COMPLETE.**

## Action 14.4 — Security oracles and measurement model

Specification:

`docs/security/fixtures/phase14-security-oracles-v1.json`

Deterministic application-security controls are separated from stochastic or
model-dependent behavior.

Model-dependent conclusions require repeated trials.

Untested attacks remain NOT_VERIFIED.

Thresholds will be established from measured results rather than invented
before a baseline exists.

**Action 14.4 status: COMPLETE.**

## Phase status

Actions complete:

**4 / 15**

Progress:

**26.7%**

Next:

**Accelerated Batch B — Actions 14.5–14.9.**

## Action 14.5 — Prompt injection, retrieval poisoning and provenance regression

Phase 10 deterministic security controls were re-executed successfully.

Regression coverage includes retrieved-content trust boundaries, indirect prompt
injection hardening, RAG poisoning and provenance/citation integrity.

These results verify supporting application controls; they do not establish
arbitrary-model prompt-injection immunity.

**Action 14.5 status: COMPLETE.**

## Action 14.6 — Cross-tenant, privacy, revocation and DLP regression

Phase 12 deterministic controls were re-executed successfully.

Coverage includes negative cross-user access, tenant/privacy boundaries,
retention/deletion and synthetic DLP/redaction/export behavior.

No stochastic sensitive-data-exposure rate is claimed yet.

**Action 14.6 status: COMPLETE.**

## Action 14.7 — Agent, Action, MCP and tool-security regression

Phase 11 deterministic controls were re-executed successfully.

Coverage includes tool authority, unknown-tool rejection, MCP security
boundaries, action approval, confused-deputy protections, untrusted tool-result
handling and credential delegation.

These results verify application controls rather than every possible
model-generated agent trajectory.

**Action 14.7 status: COMPLETE.**

## Action 14.8 — Recursion, abuse and bounded-resource regression

Phase 11 and Phase 13 bounded-execution controls were re-executed successfully.

Coverage includes tool fan-out, finite execution, duplicate-work handling,
backpressure, publication-failure rollback and bounded availability/economic
security behavior.

Execution remained local with container networking disabled.

**Action 14.8 status: COMPLETE.**

## Action 14.9 — Evaluator integrity and deterministic baseline

The evaluator-integrity regression passed.

Verified properties:

- 24 unique synthetic red-team cases;
- unexecuted cases remain NOT_VERIFIED;
- required red-team categories remain represented;
- model-dependent claims require repeated trials;
- thresholds require a measured baseline;
- exceptions require owner, reason, expiry, compensating control and rollback.

Batch B execution:

- suite files: 14 / 14 PASS
- parsed tests: 63
- unknown test counts: 0
- model-provider calls: 0
- Docker network mode: none

Classification:

`docs/security/fixtures/phase14-batch-b-regression-mapping.csv`

SUPPORTING_CONTROL_VERIFIED means that the deterministic supporting control
passed; it does not mean the full model-dependent attack class is proven
resistant.

**Action 14.9 status: COMPLETE.**

## Current Phase 14 status

Actions complete: **9 / 15**

Progress: **60.0%**

Remaining:

- 14.10 — repeated model-dependent trials;
- 14.11 — attack/security metrics;
- 14.12 — thresholds, exceptions and rollback;
- 14.13 — local release-gate integration;
- 14.14 — evaluator/evaluation-data integrity and independent cross-check;
- 14.15 — evidence manifest, residual risk and final closeout.
