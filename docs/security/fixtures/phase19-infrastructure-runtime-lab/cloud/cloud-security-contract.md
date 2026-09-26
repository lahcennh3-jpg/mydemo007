# Phase 19 Cloud Security Contract

## IAM

- Separate human and workload identities.
- Prefer workload identity over long-lived static access keys.
- Deny wildcard administrative permissions by default.
- Scope permissions to required operations and resources.
- Privilege escalation paths require explicit review.

## Network

- Databases, caches, vector stores, object stores, and internal APIs are private by default.
- Administrative ports are not Internet exposed.
- Ingress is explicitly allowed.
- Egress is constrained where technically practical.
- Service boundaries preserve tenant separation.

## Storage

- Public object access is denied by default.
- Sensitive data requires encryption at rest where supported.
- Transport encryption is required where supported.
- Important artifacts require recovery/version controls.

## Metadata

- Metadata access is blocked unless required.
- SSRF must not become a cloud credential extraction path.
- Metadata credentials must be short-lived.
- Broad node or instance credentials are prohibited for ordinary workloads.

## Secrets

- Real secrets are never committed.
- Runtime secret delivery is preferred.
- Long-lived static cloud keys are prohibited for ordinary workloads.

## Boundary

No real cloud deployment or billable resource is authorized in this lab.
