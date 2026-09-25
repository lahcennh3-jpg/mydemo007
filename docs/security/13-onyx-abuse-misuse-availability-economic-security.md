# Phase 13 — Onyx Abuse, Misuse, Availability and Economic Security

## Objective

Assess abuse resistance, misuse controls, availability boundaries,
resource exhaustion and economic/cost amplification in the approved
synthetic Onyx laboratory.

## Safety boundary

- synthetic identities and data only;
- no production systems;
- no real credentials;
- no paid external AI/API calls;
- no destructive denial-of-service testing;
- maximum 100 requests per bounded case;
- maximum 10 concurrent requests/tasks;
- maximum 60 seconds per runtime case;
- maximum 1 MiB synthetic test file;
- stop on unexpected external network activity;
- stop on scope uncertainty.

## Action 13.1 — Abuse-security scope

Coverage:

- API/request abuse;
- authentication abuse;
- rate limiting;
- quotas and admission control;
- concurrency;
- queue amplification;
- duplicate work;
- expensive-operation repetition;
- LLM/token amplification;
- RAG/search amplification;
- agent/tool/MCP fan-out;
- connector/indexing amplification;
- file-processing amplification;
- retry amplification;
- resource exhaustion;
- timeouts/cancellation;
- graceful degradation;
- economic denial of sustainability;
- abuse monitoring and response.

**Action 13.1 status: COMPLETE.**

## Action 13.2 — Rate/quota/admission inventory

Candidate source-level controls for rate limiting, quotas, concurrency,
queue depth, admission and backpressure are inventoried.

Source presence is not treated as runtime proof.

**Action 13.2 status: COMPLETE.**

## Action 13.3 — Availability/resource inventory

Candidate timeout, queue, watchdog, retry, resource-limit, cancellation
and worker controls are inventoried.

Runtime effectiveness remains unclaimed.

**Action 13.3 status: COMPLETE.**

## Action 13.4 — Economic-abuse test matrix

A bounded 16-case synthetic attack matrix is defined.

**Action 13.4 status: COMPLETE.**

## Next

Actions 13.5–13.9 perform bounded functional verification.
