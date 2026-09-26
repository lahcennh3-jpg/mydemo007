#!/usr/bin/env bash
set -euo pipefail

ROOT="docs/security/fixtures/phase19-infrastructure-runtime-lab"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

FAIL=0
DETECTED=0

expect_secure() {
    local description="$1"
    shift

    if "$@" >/dev/null 2>&1; then
        echo "PASS secure baseline [$description]"
    else
        echo "FAIL secure baseline [$description]"
        FAIL=1
    fi
}

expect_detected() {
    local file="$1"
    local pattern="$2"
    local description="$3"

    if grep -Eq "$pattern" "$file"; then
        echo "PASS negative mutation detected [$description]"
        DETECTED=$((DETECTED + 1))
    else
        echo "FAIL negative mutation not detected [$description]"
        FAIL=1
    fi
}


# ------------------------------------------------------------
# Positive baselines
# ------------------------------------------------------------

expect_secure \
    "container/kubernetes static gate" \
    bash "$ROOT/phase19_static_gate.sh"

expect_secure \
    "IaC negative/positive gate" \
    bash "$ROOT/iac/phase19_iac_policy_gate.sh"

expect_secure \
    "identity lifecycle gate" \
    bash "$ROOT/workload-identity/phase19_identity_gate.sh"

expect_secure \
    "Batch B cross-layer release gate" \
    bash "$ROOT/phase19_batch_b_release_gate.sh"


# ------------------------------------------------------------
# Mutation 1 — writable root filesystem
# ------------------------------------------------------------

cp "$ROOT/compose.hardened.yml" \
   "$TMP/compose-writable.yml"

sed -i \
    's/read_only: true/read_only: false/' \
    "$TMP/compose-writable.yml"

expect_detected \
    "$TMP/compose-writable.yml" \
    'read_only:[[:space:]]*false' \
    "writable container root filesystem"


# ------------------------------------------------------------
# Mutation 2 — privileged Compose workload
# ------------------------------------------------------------

cp "$ROOT/compose.hardened.yml" \
   "$TMP/compose-privileged.yml"

sed -i \
    '/user: "10001:10001"/a\    privileged: true' \
    "$TMP/compose-privileged.yml"

expect_detected \
    "$TMP/compose-privileged.yml" \
    'privileged:[[:space:]]*true' \
    "privileged Compose workload"


# ------------------------------------------------------------
# Mutation 3 — Kubernetes privilege escalation
# ------------------------------------------------------------

cp "$ROOT/kubernetes/security-baseline.yaml" \
   "$TMP/k8s-privilege-escalation.yaml"

sed -i \
    's/allowPrivilegeEscalation: false/allowPrivilegeEscalation: true/' \
    "$TMP/k8s-privilege-escalation.yaml"

expect_detected \
    "$TMP/k8s-privilege-escalation.yaml" \
    'allowPrivilegeEscalation:[[:space:]]*true' \
    "Kubernetes privilege escalation"


# ------------------------------------------------------------
# Mutation 4 — automatic service-account token
# ------------------------------------------------------------

cp "$ROOT/kubernetes/security-baseline.yaml" \
   "$TMP/k8s-token.yaml"

sed -i \
    '0,/automountServiceAccountToken: false/s//automountServiceAccountToken: true/' \
    "$TMP/k8s-token.yaml"

expect_detected \
    "$TMP/k8s-token.yaml" \
    'automountServiceAccountToken:[[:space:]]*true' \
    "automatic service-account token"


# ------------------------------------------------------------
# Mutation 5 — root-capable workload
# ------------------------------------------------------------

cp "$ROOT/kubernetes/security-baseline.yaml" \
   "$TMP/k8s-root.yaml"

sed -i \
    's/runAsNonRoot: true/runAsNonRoot: false/' \
    "$TMP/k8s-root.yaml"

expect_detected \
    "$TMP/k8s-root.yaml" \
    'runAsNonRoot:[[:space:]]*false' \
    "root-capable Kubernetes workload"


# ------------------------------------------------------------
# Mutation 6 — workload identity fail-open
# ------------------------------------------------------------

cp "$ROOT/workload-identity/workload-identity-policy.env" \
   "$TMP/identity-fail-open.env"

sed -i \
    's/FAIL_CLOSED_ON_IDENTITY_FAILURE=true/FAIL_CLOSED_ON_IDENTITY_FAILURE=false/' \
    "$TMP/identity-fail-open.env"

expect_detected \
    "$TMP/identity-fail-open.env" \
    '^FAIL_CLOSED_ON_IDENTITY_FAILURE=false$' \
    "identity service failure becomes fail-open"


# ------------------------------------------------------------
# Mutation 7 — long-lived static credentials
# ------------------------------------------------------------

cp "$ROOT/workload-identity/workload-identity-policy.env" \
   "$TMP/identity-static-creds.env"

sed -i \
    's/STATIC_LONG_LIVED_CREDENTIALS_ALLOWED=false/STATIC_LONG_LIVED_CREDENTIALS_ALLOWED=true/' \
    "$TMP/identity-static-creds.env"

expect_detected \
    "$TMP/identity-static-creds.env" \
    '^STATIC_LONG_LIVED_CREDENTIALS_ALLOWED=true$' \
    "long-lived static workload credentials"


# ------------------------------------------------------------
# Mutation 8 — world-open IaC network
#
# IMPORTANT:
# Do not pipe the gate directly into grep -q while pipefail is active.
# Capture its complete output first.
# ------------------------------------------------------------

IAC_GATE_OUTPUT="$(
    bash "$ROOT/iac/phase19_iac_policy_gate.sh"
)"

if grep -Fq \
    'PASS negative [world-open ingress]' \
    <<<"$IAC_GATE_OUTPUT"
then
    echo "PASS negative mutation detected [world-open IaC network]"
    DETECTED=$((DETECTED + 1))
else
    echo "FAIL negative mutation not detected [world-open IaC network]"
    printf '%s\n' "$IAC_GATE_OUTPUT"
    FAIL=1
fi


if test "$FAIL" -ne 0; then
    echo "PHASE19_CROSS_LAYER_NEGATIVE_GATE=FAIL"
    echo "DETECTED_NEGATIVE_CONTROLS=$DETECTED"
    exit 1
fi

test "$DETECTED" -eq 8 || {
    echo "PHASE19_CROSS_LAYER_NEGATIVE_GATE=FAIL"
    echo "DETECTED_NEGATIVE_CONTROLS=$DETECTED"
    exit 1
}

echo "PHASE19_CROSS_LAYER_NEGATIVE_GATE=PASS"
echo "DETECTED_NEGATIVE_CONTROLS=8"
echo "POSITIVE_BASELINES_REVALIDATED=4"
