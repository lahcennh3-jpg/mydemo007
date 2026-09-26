# Phase 19 — Final Infrastructure Security Assessment

## Scope

Phase 19 evaluates the authorized local/synthetic infrastructure-security
boundary for Onyx.

The assessed areas include:

- container security;
- Compose configuration;
- Kubernetes workload security;
- RBAC and service identity;
- network isolation;
- admission requirements;
- IaC security;
- cloud-equivalent security controls;
- workload identity;
- short-lived credentials;
- rotation and revocation;
- runtime-detection design;
- databases;
- caches;
- vector infrastructure;
- object storage;
- backup infrastructure.

No real-cloud deployment was authorized.

## Verified controls

Phase 19 produced evidence for:

- non-root container execution;
- read-only filesystem policy;
- dropped Linux capabilities;
- no-new-privileges;
- bounded resource policy;
- Kubernetes restricted workload posture;
- service-account-token minimization;
- namespace-scoped RBAC;
- default-deny networking;
- IaC negative-control detection;
- least-privilege cloud requirements;
- workload-bound identity;
- attestation requirements;
- short-lived credentials;
- rotation;
- revocation;
- fail-closed identity handling;
- runtime-detection rules;
- data-infrastructure security contracts.

## P19-RISK-01 — Credential fallback values

Static repository review found **86** lines matching selected
development/template or deployment fallback-credential patterns.

Examples include:

- `password`;
- `minioadmin`;
- `StrongPassword123!`.

This does **not** prove that a production deployment uses those credentials.

It becomes a deployment vulnerability if an insecure fallback survives into an
environment where an attacker can reach the corresponding service.

Required treatment:

- production paths should fail when mandatory secrets are absent;
- insecure fallback values should not be accepted in production;
- secrets should come from an approved runtime mechanism;
- real credentials must not be committed.

## P19-RISK-02 — Host-published data-service ports

Static repository review found **10** matching host-port configuration
lines for selected data services.

Development environments may expose services such as PostgreSQL, OpenSearch,
Redis, or MinIO to the host.

Required treatment:

- prefer loopback binding for local development;
- verify forwarded-port visibility;
- avoid unnecessary production port publication;
- use network controls around internal services.

## P19-RISK-03 — Tagged/non-digest images

Static repository review found **84** matching tagged image-reference
lines without an immutable digest.

Version tags are better than mutable `latest`, but digest pinning provides
stronger artifact identity.

Required treatment:

- tie vulnerability scanning to the released digest;
- verify provenance/signatures where required;
- pin production release artifacts where operationally appropriate.

## Environment-limited controls

Phase 19 does not claim production validation for:

1. Kubernetes CIS compliance;
2. host-kernel hardening;
3. Falco/Tetragon kernel/eBPF fidelity;
4. real-cloud IAM;
5. real-cloud networking;
6. real-cloud storage;
7. metadata-service enforcement;
8. vulnerability-free production images;
9. production artifact provenance;
10. production backup restore;
11. production workload-identity issuer/CA behavior.

## Runtime boundary

Docker runtime evidence is accepted only when the required image already exists
locally.

Phase 19 does not pull an image simply to manufacture runtime evidence.

Kubernetes server-side validation is allowed only against an explicitly
loopback cluster.

Unknown or remote clusters are not contacted.

## Final disposition

**Phase 19 local/synthetic authorized scope: COMPLETE.**

Environment-dependent controls remain documented follow-up work rather than
being misrepresented as production-verified security.

=== FALLBACK CREDENTIAL MATCHES ===
deployment/docker_compose/env.template:162:## SECURITY: minioadmin is a local-dev default. The installer randomizes it; if you
deployment/docker_compose/env.template:166:S3_AWS_ACCESS_KEY_ID=minioadmin
deployment/docker_compose/env.template:167:S3_AWS_SECRET_ACCESS_KEY=minioadmin
deployment/docker_compose/env.template:169:MINIO_ROOT_USER=minioadmin
deployment/docker_compose/env.template:170:MINIO_ROOT_PASSWORD=minioadmin
deployment/docker_compose/docker-compose.search-testing.yml:30:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.search-testing.yml:40:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
deployment/docker_compose/docker-compose.search-testing.yml:41:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
deployment/docker_compose/docker-compose.search-testing.yml:71:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.search-testing.yml:82:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
deployment/docker_compose/docker-compose.search-testing.yml:83:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
deployment/docker_compose/docker-compose.search-testing.yml:160:      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-password}
deployment/docker_compose/docker-compose.search-testing.yml:173:      - OPENSEARCH_INITIAL_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.search-testing.yml:225:      MINIO_ROOT_USER: ${MINIO_ROOT_USER:-minioadmin}
deployment/docker_compose/docker-compose.search-testing.yml:226:      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:-minioadmin}
deployment/docker_compose/docker-compose.prod.yml:42:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.prod.yml:52:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod.yml:53:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod.yml:119:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.prod.yml:129:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod.yml:130:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod.yml:363:      - OPENSEARCH_INITIAL_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.prod.yml:475:      MINIO_ROOT_USER: ${MINIO_ROOT_USER:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod.yml:476:      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.template.yml:25:#    - Set strong MinIO/S3 credentials (MINIO_ROOT_* + S3_AWS_*), not minioadmin
deployment/docker_compose/docker-compose.template.yml:100:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.template.yml:112:      #!value prod,no-letsencrypt: - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.template.yml:113:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
deployment/docker_compose/docker-compose.template.yml:114:      #!value prod,no-letsencrypt: - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.template.yml:115:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
deployment/docker_compose/docker-compose.template.yml:191:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.template.yml:203:      #!value prod,no-letsencrypt: - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.template.yml:204:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
deployment/docker_compose/docker-compose.template.yml:205:      #!value prod,no-letsencrypt: - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.template.yml:206:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
deployment/docker_compose/docker-compose.template.yml:441:      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-password}
deployment/docker_compose/docker-compose.template.yml:475:      - OPENSEARCH_INITIAL_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.template.yml:640:      #!value prod,no-letsencrypt: MINIO_ROOT_USER: ${MINIO_ROOT_USER:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.template.yml:641:      MINIO_ROOT_USER: ${MINIO_ROOT_USER:-minioadmin}
deployment/docker_compose/docker-compose.template.yml:642:      #!value prod,no-letsencrypt: MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.template.yml:643:      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:-minioadmin}
deployment/docker_compose/docker-compose.yml:20:#    - Set strong MinIO/S3 credentials (MINIO_ROOT_* + S3_AWS_*), not minioadmin
deployment/docker_compose/docker-compose.yml:87:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.yml:92:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
deployment/docker_compose/docker-compose.yml:93:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
deployment/docker_compose/docker-compose.yml:162:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.yml:167:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
deployment/docker_compose/docker-compose.yml:168:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
deployment/docker_compose/docker-compose.yml:380:      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-password}
deployment/docker_compose/docker-compose.yml:410:      - OPENSEARCH_INITIAL_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.yml:530:      MINIO_ROOT_USER: ${MINIO_ROOT_USER:-minioadmin}
deployment/docker_compose/docker-compose.yml:531:      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:-minioadmin}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:42:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:52:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:53:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:119:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:129:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:130:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:363:      - OPENSEARCH_INITIAL_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:460:      MINIO_ROOT_USER: ${MINIO_ROOT_USER:?set a strong value in .env, not minioadmin}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:461:      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:?set a strong value in .env, not minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/env.template:162:## SECURITY: minioadmin is a local-dev default. The installer randomizes it; if you
cli/internal/deploy/deployfiles/embedded/docker_compose/env.template:166:S3_AWS_ACCESS_KEY_ID=minioadmin
cli/internal/deploy/deployfiles/embedded/docker_compose/env.template:167:S3_AWS_SECRET_ACCESS_KEY=minioadmin
cli/internal/deploy/deployfiles/embedded/docker_compose/env.template:169:MINIO_ROOT_USER=minioadmin
cli/internal/deploy/deployfiles/embedded/docker_compose/env.template:170:MINIO_ROOT_PASSWORD=minioadmin
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:42:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:52:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:?set a strong value in .env, not minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:53:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:?set a strong value in .env, not minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:119:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:129:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:?set a strong value in .env, not minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:130:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:?set a strong value in .env, not minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:363:      - OPENSEARCH_INITIAL_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:475:      MINIO_ROOT_USER: ${MINIO_ROOT_USER:?set a strong value in .env, not minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:476:      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:?set a strong value in .env, not minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:20:#    - Set strong MinIO/S3 credentials (MINIO_ROOT_* + S3_AWS_*), not minioadmin
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:87:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:92:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:93:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:162:      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:167:      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:168:      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:380:      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-password}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:410:      - OPENSEARCH_INITIAL_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:530:      MINIO_ROOT_USER: ${MINIO_ROOT_USER:-minioadmin}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:531:      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:-minioadmin}

=== HOST-PORT MATCHES ===
deployment/docker_compose/docker-compose.dev.yml:57:      - "${POSTGRES_HOST_PORT:-5432}:5432"
deployment/docker_compose/docker-compose.dev.yml:66:      - "${OPENSEARCH_HOST_PORT:-9200}:9200"
deployment/docker_compose/docker-compose.dev.yml:93:      - "${REDIS_HOST_PORT:-6379}:6379"
deployment/docker_compose/docker-compose.dev.yml:99:      - "${MINIO_API_HOST_PORT:-9004}:9000"
deployment/docker_compose/docker-compose.dev.yml:100:      - "${MINIO_CONSOLE_HOST_PORT:-9005}:9001"
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml:57:      - "${POSTGRES_HOST_PORT:-5432}:5432"
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml:66:      - "${OPENSEARCH_HOST_PORT:-9200}:9200"
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml:93:      - "${REDIS_HOST_PORT:-6379}:6379"
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml:99:      - "${MINIO_API_HOST_PORT:-9004}:9000"
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml:100:      - "${MINIO_CONSOLE_HOST_PORT:-9005}:9001"

=== NON-DIGEST IMAGE MATCHES ===
deployment/docker_compose/docker-compose.mcp-oauth-test.yml:12:    image: onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}
deployment/docker_compose/docker-compose.mcp-oauth-test.yml:43:    image: onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}
deployment/docker_compose/docker-compose.search-testing.yml:5:    image: onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}
deployment/docker_compose/docker-compose.search-testing.yml:52:    image: onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}
deployment/docker_compose/docker-compose.search-testing.yml:96:    image: onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}
deployment/docker_compose/docker-compose.search-testing.yml:118:    image: onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}
deployment/docker_compose/docker-compose.search-testing.yml:135:    image: onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}
deployment/docker_compose/docker-compose.search-testing.yml:154:    image: postgres:15.2-alpine
deployment/docker_compose/docker-compose.search-testing.yml:169:    image: opensearchproject/opensearch:3.6.0
deployment/docker_compose/docker-compose.search-testing.yml:192:    image: nginx:1.25.5-alpine
deployment/docker_compose/docker-compose.search-testing.yml:218:    image: minio/minio:RELEASE.2025-07-23T15-54-02Z-cpuv1
deployment/docker_compose/docker-compose.search-testing.yml:238:    image: redis:7.4-alpine
deployment/docker_compose/docker-compose.mcp-api-key-test.yml:5:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:latest}
deployment/docker_compose/docker-compose.craft.yml:69:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.craft.yml:141:    image: ${SANDBOX_CONTAINER_IMAGE:-onyxdotapp/sandbox:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod.yml:11:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod.yml:87:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod.yml:161:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod.yml:241:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod.yml:285:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod.yml:331:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
deployment/docker_compose/docker-compose.prod.yml:353:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
deployment/docker_compose/docker-compose.prod.yml:392:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
deployment/docker_compose/docker-compose.prod.yml:462:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
deployment/docker_compose/docker-compose.prod.yml:472:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/minio/minio:RELEASE.2025-07-23T15-54-02Z-cpuv1
deployment/docker_compose/docker-compose.prod.yml:491:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
deployment/docker_compose/docker-compose.template.yml:54:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.template.yml:155:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.template.yml:245:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.template.yml:325:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.template.yml:376:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.template.yml:430:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
deployment/docker_compose/docker-compose.template.yml:465:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
deployment/docker_compose/docker-compose.template.yml:504:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
deployment/docker_compose/docker-compose.template.yml:602:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
deployment/docker_compose/docker-compose.template.yml:624:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/minio/minio:RELEASE.2025-07-23T15-54-02Z-cpuv1
deployment/docker_compose/docker-compose.template.yml:660:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:5:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:latest}
deployment/docker_compose/docker-compose.yml:48:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.yml:130:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.yml:202:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.yml:282:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.yml:325:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.yml:370:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
deployment/docker_compose/docker-compose.yml:400:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
deployment/docker_compose/docker-compose.yml:439:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
deployment/docker_compose/docker-compose.yml:499:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
deployment/docker_compose/docker-compose.yml:517:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/minio/minio:RELEASE.2025-07-23T15-54-02Z-cpuv1
deployment/docker_compose/docker-compose.yml:547:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:11:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:87:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:161:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:241:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:285:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:331:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:353:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:392:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:447:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:457:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/minio/minio:RELEASE.2025-07-23T15-54-02Z-cpuv1
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:476:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml:69:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml:141:    image: ${SANDBOX_CONTAINER_IMAGE:-onyxdotapp/sandbox:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:11:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:87:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:161:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:241:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:285:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:331:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:353:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:392:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:462:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:472:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/minio/minio:RELEASE.2025-07-23T15-54-02Z-cpuv1
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml:491:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:48:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:130:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:202:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:282:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:325:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:370:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:400:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:439:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:499:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:517:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/minio/minio:RELEASE.2025-07-23T15-54-02Z-cpuv1
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml:547:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
