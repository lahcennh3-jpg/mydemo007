# Phase 24 — Batch B Auth/Authz/Tenant/RAG Runtime Evidence

Timestamp UTC: 2026-09-26T16:55:50Z

SOURCE_HEAD=970aab202266369ab63af6fc0315039c9e7823a4

RUNNER_SHA256=b06da5333ef99131054a502cb38c1616f21691409f646a13ee794d29d4577610

TEST_TARGET=http://api_server:8080

NETWORK_SCOPE=INTERNAL_ONLY

BATCH_B_CLIENT_EXTERNAL_NETWORK=DENIED

SYNTHETIC_DATA_ONLY=YES

RAW_RESPONSE_BODIES_STORED=NO

COOKIES_STORED=NO

PASSWORDS_STORED=NO

## EV23-001 — Authentication negative paths

EV23-001=PASS

Runtime cases:

- unauthenticated /me;
- invalid synthetic session cookie;
- invalid synthetic credentials;
- valid synthetic login positive control.

ACTION_24.7=PASS_AUTHENTICATION_RUNTIME

## EV23-002 — Object ownership / BOLA

EV23-002=INCONCLUSIVE

Runtime cases:

- synthetic owner creates chat;
- owner reads object;
- second authenticated user attempts read;
- second authenticated user attempts delete;
- owner re-reads object after unauthorized delete attempt.

ACTION_24.8=INCONCLUSIVE_BOLA_RUNTIME

## EV23-003 — Tenant isolation

EV23-003=BLOCKED

Reason:

SECOND_TENANT_FIXTURE_NOT_ESTABLISHED=YES

The current reconstructed control-plane baseline does not contain a second
tenant fixture. Cross-user evidence must not be represented as cross-tenant
evidence.

## EV23-004 — RAG authorization/revocation

EV23-004=BLOCKED

Reason:

MODEL_DEPENDENT_SECURITY_VALIDATION_COMPLETE=NO

The accepted Batch A runtime intentionally disabled the model server and uses a
synthetic tokenizer cache. Semantic retrieval/revocation validation therefore
requires a later controlled RAG runtime.

## Batch result

CURRENT_RUNTIME_REGRESSION_EXECUTED=2

BATCH_B_RUNTIME_PASS_FAMILIES=1

BATCH_B_RUNTIME_FAIL_FAMILIES=0

BATCH_B_RUNTIME_INCONCLUSIVE_FAMILIES=1

BATCH_B_BLOCKED_FAMILIES=2

PHASE24_BATCH_B=COMPLETE_WITH_INCONCLUSIVE_RESULTS

CURRENT_RUNTIME_REGRESSION_COMPLETE=NO

ACTION_24.10=PASS_BATCH_B_EVIDENCE_CHECKPOINT

NEXT=BATCH_B_RETEST_REQUIRED_THEN_BATCH_C
