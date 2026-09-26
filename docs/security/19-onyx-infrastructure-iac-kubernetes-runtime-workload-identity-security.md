# Phase 19 — Onyx Container, Kubernetes, Cloud, IaC, Runtime, and Workload-Identity Security

## Execution state

- Phase: 19
- Mode: accelerated
- Branch: `security/phase-19-infrastructure-iac-kubernetes-runtime-workload-identity`
- Immutable Phase 18 parent SHA: `d43543898301cf877b376cdb4f293cdb5684373c`
- Production authorization: **FALSE**
- Real-cloud authorization: **FALSE**
- Real credentials/data: **PROHIBITED**
- Synthetic/local testing: **AUTHORIZED**
- Current state: **BATCH_A_COMPLETE**

## Objective

Assess and harden the infrastructure security boundary supporting Onyx,
including container construction, container runtime configuration, Docker
Compose, Kubernetes identity and authorization, pod security, network
isolation, admission policy, infrastructure as code, cloud-equivalent
configuration, runtime detection, workload identity, and supporting data
infrastructure.

## Execution fidelity

The phase intentionally separates:

1. source/configuration evidence;
2. policy-as-code evidence;
3. bounded container-runtime evidence;
4. Kubernetes control-plane/runtime evidence;
5. kernel/eBPF evidence;
6. real-cloud-provider evidence.

Evidence from one category is not treated as proof of another.

## Batch A

| Action | Objective | State |
|---|---|---|
| 19.1 | Immutable Phase 18 → Phase 19 handoff | COMPLETE |
| 19.2 | Execution-environment capability gate | COMPLETE |
| 19.3 | Infrastructure/configuration inventory | COMPLETE |
| 19.4 | Container-image hardening baseline | COMPLETE |
| 19.5 | Runtime least privilege/read-only/capability controls | COMPLETE |
| 19.6 | Compose network/resource/security controls | COMPLETE |
| 19.7 | Kubernetes namespace/SA/RBAC/pod security | COMPLETE |
| 19.8 | NetworkPolicy/admission-control baseline | COMPLETE |
| 19.9 | Image vulnerability/provenance assessment | COMPLETE_WITH_LIMITS |
| 19.10 | CIS/container/Kubernetes benchmark interpretation | COMPLETE_WITH_LIMITS |
| 19.11 | Terraform/IaC misconfiguration assessment | COMPLETE |
| 19.12 | Cloud IAM/network/storage/metadata controls | COMPLETE_WITH_LIMITS |
| 19.13 | Workload identity architecture | COMPLETE |
| 19.14 | Attestation and short-lived credential controls | COMPLETE |
| 19.15 | Rotation/revocation/fail-closed identity | COMPLETE |
| 19.16 | Runtime detection/Falco/Tetragon capability | COMPLETE_WITH_LIMITS |
| 19.17 | DB/cache/vector/object-store/backup security | COMPLETE |
| 19.18 | Remediation/policy-as-code release gate | COMPLETE |
| 19.19 | Cross-layer negative tests | PENDING |
| 19.20 | Bounded container-runtime validation | PENDING |
| 19.21 | Kubernetes/runtime validation where supported | PENDING |
| 19.22 | Final evidence-integrity manifest | PENDING |
| 19.23 | Final security assessment/gaps | PENDING |
| 19.24 | Final commit/push/ancestry/clean-tree gate | PENDING |

## Container controls

The hardened reference configuration requires:

- explicit non-root execution;
- read-only root filesystems;
- dropped Linux capabilities;
- no-new-privileges;
- PID limits;
- CPU limits;
- memory limits;
- bounded temporary writable storage.

## Docker Compose controls

The reference service uses an internal network and does not require:

- privileged execution;
- host networking;
- unrestricted process creation;
- unrestricted CPU/memory;
- embedded real credentials.

## Kubernetes controls

The reference Kubernetes configuration defines:

- restricted Pod Security admission labels;
- dedicated service account;
- disabled automatic service-account token mounting;
- namespace-scoped RBAC;
- no cluster-admin role;
- no secret-reading permission;
- non-root execution;
- RuntimeDefault seccomp;
- disabled privilege escalation;
- dropped capabilities;
- read-only root filesystem;
- resource requests and limits;
- default-deny NetworkPolicy.

## Admission contract

The baseline admission contract prohibits or constrains:

- mutable production image tags;
- privileged containers;
- host namespaces;
- privilege escalation;
- root workloads;
- unnecessary capabilities;
- missing resource controls;
- unnecessary service-account tokens;
- cluster-admin grants;
- hostPath volumes;
- missing network isolation;
- secrets embedded in manifests.

## Interrupted-run handling

The original Batch A harness required `python3`, but the active Codespace did
not provide that command.

The security requirements were not weakened or skipped. The same assertions
were reimplemented as a shell-only deterministic static gate, avoiding an
unnecessary package installation and preserving the zero-cost/minimal-change
execution boundary.

## Evidence

- `docs/security/evidence/phase19-action-19.1-immutable-start-gate.txt`
- `docs/security/evidence/phase19-action-19.2-environment-capability-gate.txt`
- `docs/security/evidence/phase19-action-19.3-infrastructure-surface-inventory.txt`
- `docs/security/evidence/phase19-batch-a-resume-environment-fallback.txt`
- `docs/security/evidence/phase19-actions-19.4-19.8-security-baseline-review.txt`
- `docs/security/evidence/phase19-actions-19.4-19.8-static-security-tests.txt`
- `docs/security/fixtures/phase19-infrastructure-runtime-lab/phase19_static_gate.sh`
- `docs/security/fixtures/phase19-infrastructure-runtime-lab/Dockerfile.hardened.example`
- `docs/security/fixtures/phase19-infrastructure-runtime-lab/compose.hardened.yml`
- `docs/security/fixtures/phase19-infrastructure-runtime-lab/kubernetes/security-baseline.yaml`
- `docs/security/fixtures/phase19-infrastructure-runtime-lab/kubernetes/admission-policy-contract.md`

## Batch A conclusion

The immutable Phase 18 → Phase 19 transition and the first infrastructure
security baseline are complete.

The current evidence supports configuration and policy-level conclusions only.

It does not claim production Kubernetes, kernel/eBPF, or real-cloud security
validation.

NEXT=PHASE19_ACCELERATED_BATCH_B

## Batch B — Actions 19.9–19.18

Batch B evaluated the infrastructure-security controls that follow the initial
container and Kubernetes baseline.

### 19.9 — Image vulnerability and provenance

Image references were inventoried without pulling new images or authenticating
to external registries.

Digest-pinned references are distinguished from non-digest references.

Availability of Trivy, Cosign, Syft, and Docker is recorded separately from any
security claim.

No vulnerability-free or signed-provenance claim is made without actual tool
evidence.

### 19.10 — CIS benchmark interpretation

Codespaces can support configuration and manifest analysis but is not treated
as authoritative evidence for host-kernel or production Kubernetes CIS
compliance.

### 19.11 — Infrastructure as code

Synthetic negative controls verify detection of world-open ingress, public
storage, wildcard authorization, and hardcoded credentials.

The corresponding secure fixture must exclude those conditions.

No Terraform apply is performed.

### 19.12 — Cloud controls

Provider-neutral security requirements cover least-privilege IAM, private
networking, private storage, metadata credential protection, encryption, and
prohibition of ordinary long-lived workload credentials.

No real cloud resource was created.

### 19.13–19.15 — Workload identity

The Phase 19 synthetic identity model requires workload-bound identity,
attestation, short-lived credentials, pre-expiry rotation, revocation, and
fail-closed behavior.

A permanent fallback credential is prohibited.

### 19.16 — Runtime detection

Reference detections cover container shell execution, writes below `/etc`, and
metadata-endpoint access.

These rules do not constitute kernel/eBPF validation.

### 19.17 — Data infrastructure

Security contracts cover databases, caches, vector stores, object storage, and
backup infrastructure.

Authentication, least privilege, network isolation, tenant isolation,
integrity, retention, and restore validation remain required.

### 19.18 — Release gate

The Batch B release gate verifies presence of the expected controls across the
container, Kubernetes, IaC, cloud, identity, runtime-detection, and
data-infrastructure layers.

A PASS applies only to the authorized synthetic/configuration scope.

It does not claim:

- production Kubernetes security;
- production CIS compliance;
- real-cloud security;
- successful eBPF detection;
- vulnerability-free production images.

## Batch B evidence

- `docs/security/evidence/phase19-action-19.9-image-vulnerability-provenance-assessment.txt`
- `docs/security/evidence/phase19-action-19.10-cis-benchmark-interpretation.txt`
- `docs/security/evidence/phase19-action-19.11-iac-terraform-assessment.txt`
- `docs/security/evidence/phase19-action-19.12-cloud-security-controls.txt`
- `docs/security/evidence/phase19-action-19.13-workload-identity-architecture.txt`
- `docs/security/evidence/phase19-action-19.14-attestation-short-lived-credentials.txt`
- `docs/security/evidence/phase19-action-19.15-rotation-revocation-fail-closed.txt`
- `docs/security/evidence/phase19-action-19.16-runtime-detection-assessment.txt`
- `docs/security/evidence/phase19-action-19.17-data-infrastructure-security.txt`
- `docs/security/evidence/phase19-action-19.18-policy-release-gate.txt`

NEXT=PHASE19_ACCELERATED_BATCH_C
