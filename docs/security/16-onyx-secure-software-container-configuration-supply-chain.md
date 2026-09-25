# Phase 16 — Secure Software, Container, and Configuration Supply Chain

## Objective

Establish verifiable controls protecting the software, dependency,
container, CI/CD, configuration, build, release, and artifact supply chain
for the Onyx security assessment project.

## Safety boundary

Testing is restricted to authorized project resources and synthetic/local
evidence.

No production compromise, external dependency compromise, credential abuse,
or destructive supply-chain testing is authorized.

---

## Action 16.1 — Immutable Phase 15 handoff

Status: COMPLETE

Validated the Phase 15 parent branch, immutable parent commit, and Phase 16
branch creation.

## Action 16.2 — Secure development and change-control inventory

Status: COMPLETE

Inventoried repository workflow, review, policy, contribution, security,
dependency-management, and automation controls.

Repository inventory does not by itself prove that remote repository
enforcement or production approval controls are enabled.

## Action 16.3 — Dependency and lock-file inventory

Status: COMPLETE

Inventoried dependency manifests and available lock artifacts to establish
the dependency-control baseline.

## Action 16.4 — Secret-scanning baseline

Status: COMPLETE

Executed a bounded repository-local redacted pattern scan.

The Codespace did not provide Python 3, so a shell/awk fallback was used.

Potential matches are review items and are not automatically classified as
vulnerabilities.

Secret values were not intentionally copied into evidence.

## Action 16.5 — Static-analysis baseline

Status: COMPLETE

Executed bounded local source-code security heuristics.

The shell heuristic checks are evidence-generation controls. They are not
represented as equivalent to Semgrep or a complete commercial/enterprise
SAST assessment.

## Action 16.6 — CI, container, and configuration integrity baseline

Status: COMPLETE

Inventoried CI workflow, container, infrastructure, and deployment
configuration artifacts.

Generated SHA-256 integrity evidence for identified supply-chain-sensitive
files.

---

## Batch A result

Actions 16.1–16.6 complete.

Next:

- 16.7 dependency vulnerability and license analysis
- 16.8 container/image security
- 16.9 IaC/configuration security
- 16.10 SBOM generation and validation
- 16.11 artifact signing and attestations
- 16.12 build provenance and reproducibility

Current conclusion:

PHASE_16_BATCH_A_COMPLETE

<!-- PHASE16_BATCH_B_START -->

---

## Action 16.7 — Dependency vulnerability and license analysis

Status: COMPLETE WITH TOOLING LIMITATION

Dependency artifacts analyzed: 28

Pinning review findings: 6

A vulnerability-database-backed CVE scan was not executed because an approved
local vulnerability scanner/database is unavailable.

No network vulnerability lookup was performed.

## Action 16.8 — Container and image security

Status: COMPLETE WITH REVIEW

Dockerfiles reviewed: 9

Compose files reviewed: 22

Container review findings: 56

No remote image pull or unverified image CVE claim was made.

## Action 16.9 — IaC and configuration security

Status: COMPLETE WITH REVIEW

IaC/configuration files reviewed: 189

Review findings: 37

Findings are triage candidates, not automatically confirmed vulnerabilities.

## Action 16.10 — SBOM and component inventory

Status: COMPLETE WITH DOCUMENTED LIMITATION

Offline SBOM-lite rows: 1393

SBOM SHA-256:

b94f0b640f00e8e5c9b0c336cb412d15855f37a9e4037be3019b15741adc328d

Syft was unavailable, so this artifact is not represented as a complete
CycloneDX or SPDX SBOM.

## Action 16.11 — Artifact attestation and signing

Status: COMPLETE FOR LOCAL DEMONSTRATION SCOPE

Signature status:

VERIFIED

The signing private key was ephemeral and was not stored in the repository.

This demonstration is not represented as a production Cosign/Sigstore trust
chain.

## Action 16.12 — Provenance and reproducibility

Status: COMPLETE FOR SOURCE-PROVENANCE SCOPE

Supply-chain input integrity:

PASS

Source archive A:

3e477fe5ea7e8d1afc239ce4fd2d3f4428877c7f1fb5f07e9f3137bcee5bd1fb

Source archive B:

3e477fe5ea7e8d1afc239ce4fd2d3f4428877c7f1fb5f07e9f3137bcee5bd1fb

Source archive reproducibility:

YES

This demonstrates deterministic Git source archive generation only. It does
not prove reproducible container binaries or dependency builds.

---

## Batch B result

Actions 16.7–16.12 complete.

Progress:

12 / 15 actions

80%

Remaining:

- 16.13 release manifest and fail-closed release gate
- 16.14 exception, rollback, revocation, and recovery controls
- 16.15 regression verification and final Phase 16 closeout

PHASE_16_BATCH_B_COMPLETE

<!-- PHASE16_BATCH_B_END -->
