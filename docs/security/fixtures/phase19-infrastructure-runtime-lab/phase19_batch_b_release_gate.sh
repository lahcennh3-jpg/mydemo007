#!/usr/bin/env bash
set -u

ROOT="docs/security/fixtures/phase19-infrastructure-runtime-lab"
FAIL=0

required_files=(
"$ROOT/Dockerfile.hardened.example"
"$ROOT/compose.hardened.yml"
"$ROOT/kubernetes/security-baseline.yaml"
"$ROOT/kubernetes/admission-policy-contract.md"
"$ROOT/iac/insecure-example.tf.disabled"
"$ROOT/iac/secure-example.tf.disabled"
"$ROOT/cloud/cloud-security-contract.md"
"$ROOT/workload-identity/workload-identity-policy.env"
"$ROOT/workload-identity/workload-identity-contract.md"
"$ROOT/runtime-detection/falco-reference-rules.yaml"
"$ROOT/data-infrastructure/data-infrastructure-security-contract.md"
)

for f in "${required_files[@]}"; do
    if test -f "$f"; then
        echo "PASS file $f"
    else
        echo "FAIL missing $f"
        FAIL=1
    fi
done

require() {
    local file="$1"
    local token="$2"
    local label="$3"

    if grep -Fq -- "$token" "$file"; then
        echo "PASS [$label]"
    else
        echo "FAIL [$label]"
        FAIL=1
    fi
}

require "$ROOT/compose.hardened.yml" \
    "read_only: true" \
    "read-only rootfs"

require "$ROOT/compose.hardened.yml" \
    "cap_drop:" \
    "capability reduction"

require "$ROOT/kubernetes/security-baseline.yaml" \
    "runAsNonRoot: true" \
    "non-root pod"

require "$ROOT/kubernetes/security-baseline.yaml" \
    "automountServiceAccountToken: false" \
    "SA token minimization"

require "$ROOT/kubernetes/security-baseline.yaml" \
    "name: default-deny" \
    "network default deny"

require "$ROOT/cloud/cloud-security-contract.md" \
    "Public object access is denied by default." \
    "private object storage"

require "$ROOT/workload-identity/workload-identity-policy.env" \
    "ATTESTATION_REQUIRED=true" \
    "attestation"

require "$ROOT/workload-identity/workload-identity-policy.env" \
    "STATIC_LONG_LIVED_CREDENTIALS_ALLOWED=false" \
    "static credential prohibition"

require "$ROOT/workload-identity/workload-identity-policy.env" \
    "FAIL_CLOSED_ON_IDENTITY_FAILURE=true" \
    "identity fail closed"

require "$ROOT/data-infrastructure/data-infrastructure-security-contract.md" \
    "Restore testing is required." \
    "backup restore testing"

if test "$FAIL" -ne 0; then
    echo "PHASE19_BATCH_B_RELEASE_GATE=FAIL"
    exit 1
fi

echo "PHASE19_BATCH_B_RELEASE_GATE=PASS"
echo "CONTAINER_POLICY=PASS"
echo "KUBERNETES_POLICY=PASS"
echo "IAC_POLICY=PASS"
echo "CLOUD_POLICY=PASS"
echo "WORKLOAD_IDENTITY_POLICY=PASS"
echo "DATA_INFRASTRUCTURE_POLICY=PASS"
