# Phase 24 — Bounded Dependency Image Recovery

Timestamp UTC: 2026-09-26T16:21:53Z

## Reason

The Codespaces Docker cache no longer contained all infrastructure images.

The first Phase 24 runtime recovery stopped on:

`redis:7.4-alpine`

No uncontrolled pull was performed by that attempt.

## Recovery scope

Network retrieval was permitted only for the following Compose-pinned
infrastructure images when absent locally:

- redis:7.4-alpine
- opensearchproject/opensearch:3.6.0

The following protected images were required to remain locally available and
were not automatically retrieved:

- postgres:15.2-alpine
- onyxdotapp/onyx-backend:latest

## Resulting identities

REDIS_IMAGE=redis:7.4-alpine

REDIS_IMAGE_ID=sha256:858f009f9709ce576febc734aa78b8f6d624b82571f9ddb6bda4377c833b3499

REDIS_REPO_DIGEST=redis@sha256:858f009f9709ce576febc734aa78b8f6d624b82571f9ddb6bda4377c833b3499

OPENSEARCH_IMAGE=opensearchproject/opensearch:3.6.0

OPENSEARCH_IMAGE_ID=sha256:b5dd1512af2a99748c942cfbbd7f32162623336b210667d0fc6333c6321f171d

OPENSEARCH_REPO_DIGEST=opensearchproject/opensearch@sha256:b5dd1512af2a99748c942cfbbd7f32162623336b210667d0fc6333c6321f171d

POSTGRES_IMAGE=postgres:15.2-alpine

POSTGRES_IMAGE_ID=sha256:d9c304353c031b21e9a7e33dc4781e272a9fa802a2ab9703fe4199d72ba1422c

BACKEND_IMAGE=onyxdotapp/onyx-backend:latest

BACKEND_IMAGE_ID=sha256:fa570e141e39af5e1e48767fe14cbe227abe9a5ec0e3d08b9580c8bf60b35543

APPLICATION_IMAGE_PULL=NO

APPLICATION_IMAGE_SUBSTITUTION=NO

AUTOMATIC_ONYX_UPGRADE=NO

## Runtime continuity

The failed Compose restoration created fresh database and OpenSearch volumes.

Therefore:

RUNTIME_BASELINE_TYPE=RECONSTRUCTED

PRIOR_RUNTIME_DATA_CONTINUITY=NOT_ESTABLISHED

OLD_RUNTIME_SECURITY_RESULT_INHERITANCE=NO

Fresh runtime testing is required.

IMAGE_RECOVERY_GATE=PASS

## Local authentication-secret reconstruction

Timestamp UTC: 2026-09-26T16:30:35Z

The reconstructed runtime initially failed closed because USER_AUTH_SECRET
was empty.

A fresh synthetic local secret was generated for the authorized lab using
openssl and stored only in the Git-ignored Docker Compose .env file.

USER_AUTH_SECRET_PROVISIONED=YES

USER_AUTH_SECRET_LENGTH=64

USER_AUTH_SECRET_VALUE_DISCLOSED=NO

USER_AUTH_SECRET_COMMITTED=NO

SECRET_SCOPE=LOCAL_SYNTHETIC_LAB_ONLY

## Model-server startup dependency resolution

Timestamp UTC: 2026-09-26T16:35:41Z

The reconstructed API passed USER_AUTH_SECRET validation but failed during
startup because inference_model_server was absent.

For the Phase 24 control-plane baseline, the supported Onyx environment flag:

DISABLE_MODEL_SERVER=true

was enabled in the Git-ignored local Compose .env.

No model-server image was downloaded.

No model was downloaded.

No external model provider was contacted intentionally.

MODEL_SERVER_MODE=DISABLED_FOR_CONTROL_PLANE_BASELINE

MODEL_SERVER_IMAGE_PULL=NO

MODEL_DOWNLOAD=NO

MODEL_DEPENDENT_SECURITY_VALIDATION_COMPLETE=NO

This setting is sufficient only for establishing the API/control-plane
runtime baseline.

It does not satisfy later model, embedding, reranking, semantic retrieval,
or generation-dependent security evaluations.

## Outbound-network stop event

Timestamp UTC: 2026-09-26T16:42:21Z

During the previous interrupted startup, tokenizer initialization emitted a
Hugging Face Hub network warning.

That startup is not accepted as the Phase 24 security-test baseline.

UNEXPECTED_EXTERNAL_CALL_OBSERVED=YES

OUTBOUND_DESTINATION_CLASS=HUGGINGFACE_HUB

CAUSE=TOKENIZER_INITIALIZATION

INTERRUPTED_RUNTIME_ACCEPTED_FOR_SECURITY_PASS=NO

REMEDIATION_REQUIRED=YES

## Compose compatibility repair

Timestamp UTC: 2026-09-26T16:48:19Z

The preceding attempt stopped before API creation because this Docker Compose
version does not accept --no-deps with the create command.

The corrected flow used:

docker compose up --no-start --no-deps

The API process therefore remained stopped while automatic networks were
removed and the internal-only Phase 24 network was attached.

COMPOSE_CREATE_NO_DEPS_SUPPORTED=NO

COMPOSE_UP_NO_START_USED=YES

PRESTART_NETWORK_ISOLATION_USED=YES

API_STARTED_WITH_DEFAULT_OUTBOUND_NETWORK=NO
