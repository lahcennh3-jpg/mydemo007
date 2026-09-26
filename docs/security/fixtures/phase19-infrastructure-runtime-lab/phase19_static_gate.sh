#!/usr/bin/env bash
set -u

ROOT="docs/security/fixtures/phase19-infrastructure-runtime-lab"

DOCKERFILE="$ROOT/Dockerfile.hardened.example"
COMPOSE="$ROOT/compose.hardened.yml"
K8S="$ROOT/kubernetes/security-baseline.yaml"
CONTRACT="$ROOT/kubernetes/admission-policy-contract.md"

FAILURES=0

require() {
    local file="$1"
    local token="$2"
    local label="$3"

    if grep -Fq -- "$token" "$file"; then
        echo "PASS [$label]"
    else
        echo "FAIL [$label] missing: $token"
        FAILURES=$((FAILURES + 1))
    fi
}

forbid() {
    local file="$1"
    local token="$2"
    local label="$3"

    if grep -Fiq -- "$token" "$file"; then
        echo "FAIL [$label] forbidden value found: $token"
        FAILURES=$((FAILURES + 1))
    else
        echo "PASS [$label]"
    fi
}

for f in "$DOCKERFILE" "$COMPOSE" "$K8S" "$CONTRACT"; do
    if test ! -f "$f"; then
        echo "FAIL missing fixture: $f"
        FAILURES=$((FAILURES + 1))
    fi
done

echo
echo "=== CONTAINER IMAGE ==="

require "$DOCKERFILE" \
    "USER 10001:10001" \
    "non-root image user"

forbid "$DOCKERFILE" \
    "USER root" \
    "root image user"


echo
echo "=== DOCKER COMPOSE ==="

require "$COMPOSE" \
    'user: "10001:10001"' \
    "explicit runtime user"

require "$COMPOSE" \
    "read_only: true" \
    "read-only root filesystem"

require "$COMPOSE" \
    "cap_drop:" \
    "capability configuration"

require "$COMPOSE" \
    "- ALL" \
    "drop all capabilities"

require "$COMPOSE" \
    "no-new-privileges:true" \
    "no-new-privileges"

require "$COMPOSE" \
    "internal: true" \
    "internal network"

require "$COMPOSE" \
    "pids_limit:" \
    "PID limit"

require "$COMPOSE" \
    "mem_limit:" \
    "memory limit"

require "$COMPOSE" \
    "cpus:" \
    "CPU limit"

forbid "$COMPOSE" \
    "privileged: true" \
    "privileged compose workload"

forbid "$COMPOSE" \
    "network_mode: host" \
    "host network compose workload"


echo
echo "=== KUBERNETES ==="

require "$K8S" \
    "pod-security.kubernetes.io/enforce: restricted" \
    "Pod Security restricted"

require "$K8S" \
    "automountServiceAccountToken: false" \
    "service-account token minimization"

require "$K8S" \
    "runAsNonRoot: true" \
    "run as non-root"

require "$K8S" \
    "allowPrivilegeEscalation: false" \
    "disable privilege escalation"

require "$K8S" \
    "readOnlyRootFilesystem: true" \
    "read-only root filesystem"

require "$K8S" \
    "seccompProfile:" \
    "seccomp configured"

require "$K8S" \
    "type: RuntimeDefault" \
    "RuntimeDefault seccomp"

require "$K8S" \
    "capabilities:" \
    "capability policy"

require "$K8S" \
    "drop:" \
    "capability drop"

require "$K8S" \
    "kind: NetworkPolicy" \
    "network policy"

require "$K8S" \
    "name: default-deny" \
    "default-deny policy"

require "$K8S" \
    "requests:" \
    "resource requests"

require "$K8S" \
    "limits:" \
    "resource limits"

require "$K8S" \
    "@sha256:" \
    "image digest reference"

forbid "$K8S" \
    "privileged: true" \
    "privileged Kubernetes workload"

forbid "$K8S" \
    "hostNetwork: true" \
    "host networking"

forbid "$K8S" \
    "hostPID: true" \
    "host PID"

forbid "$K8S" \
    "hostIPC: true" \
    "host IPC"

forbid "$K8S" \
    "automountServiceAccountToken: true" \
    "automatic service-account token"

forbid "$K8S" \
    "hostPath:" \
    "hostPath volume"


echo
echo "=== ADMISSION CONTRACT ==="

require "$CONTRACT" \
    'mutable `latest` tags' \
    "mutable-tag prohibition"

require "$CONTRACT" \
    "Privileged containers are prohibited" \
    "privileged-container prohibition"

require "$CONTRACT" \
    "Privilege escalation must be disabled" \
    "privilege-escalation policy"

require "$CONTRACT" \
    "run as non-root" \
    "non-root policy"

require "$CONTRACT" \
    "capabilities are dropped" \
    "capability policy"

require "$CONTRACT" \
    "network policy defaults to deny" \
    "default-deny policy"

require "$CONTRACT" \
    "Secrets must not be embedded" \
    "committed-secret prohibition"


echo

if test "$FAILURES" -ne 0; then
    echo "PHASE19_STATIC_GATE=FAIL"
    echo "FAILURE_COUNT=$FAILURES"
    exit 1
fi

echo "PHASE19_STATIC_GATE=PASS"
echo "FAILURE_COUNT=0"
echo "CONTAINER_NON_ROOT=PASS"
echo "READ_ONLY_ROOTFS=PASS"
echo "CAPABILITY_REDUCTION=PASS"
echo "NO_NEW_PRIVILEGES=PASS"
echo "COMPOSE_INTERNAL_NETWORK=PASS"
echo "RESOURCE_LIMITS=PASS"
echo "K8S_POD_SECURITY=PASS"
echo "K8S_SERVICE_ACCOUNT_MINIMIZATION=PASS"
echo "K8S_RBAC_BASELINE=PASS"
echo "K8S_SECCOMP=PASS"
echo "K8S_DEFAULT_DENY_NETWORK_POLICY=PASS"
echo "IMAGE_DIGEST_REFERENCE=PASS"
echo "ADMISSION_POLICY_CONTRACT=PASS"
