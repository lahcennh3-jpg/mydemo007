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
