#!/usr/bin/env bash
set -u

BAD="docs/security/fixtures/phase19-infrastructure-runtime-lab/iac/insecure-example.tf.disabled"
GOOD="docs/security/fixtures/phase19-infrastructure-runtime-lab/iac/secure-example.tf.disabled"

FAIL=0
HITS=0

detect_bad() {
    local pattern="$1"
    local label="$2"

    if grep -Eq "$pattern" "$BAD"; then
        echo "PASS negative [$label]"
        HITS=$((HITS + 1))
    else
        echo "FAIL negative [$label]"
        FAIL=1
    fi
}

exclude_good() {
    local pattern="$1"
    local label="$2"

    if grep -Eq "$pattern" "$GOOD"; then
        echo "FAIL secure fixture [$label]"
        FAIL=1
    else
        echo "PASS secure fixture [$label]"
    fi
}

detect_bad '0\.0\.0\.0/0' "world-open ingress"
detect_bad 'public[[:space:]]*=[[:space:]]*true' "public storage"
detect_bad 'actions[[:space:]]*=[[:space:]]*\["\*"\]' "wildcard actions"
detect_bad 'resources[[:space:]]*=[[:space:]]*\["\*"\]' "wildcard resources"
detect_bad 'hardcoded_password' "hardcoded credential"

exclude_good '0\.0\.0\.0/0' "world-open ingress"
exclude_good 'public[[:space:]]*=[[:space:]]*true' "public storage"
exclude_good 'actions[[:space:]]*=[[:space:]]*\["\*"\]' "wildcard actions"
exclude_good 'resources[[:space:]]*=[[:space:]]*\["\*"\]' "wildcard resources"
exclude_good 'hardcoded_password' "hardcoded credential"

if test "$FAIL" -ne 0 || test "$HITS" -lt 5; then
    echo "PHASE19_IAC_GATE=FAIL"
    exit 1
fi

echo "PHASE19_IAC_GATE=PASS"
echo "NEGATIVE_CONTROLS_DETECTED=$HITS"
