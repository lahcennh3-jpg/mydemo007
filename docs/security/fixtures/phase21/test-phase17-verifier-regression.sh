#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"

VERIFIER_REL="docs/security/fixtures/phase17-ai-artifact-lab/tools/verify-phase17-pipeline.sh"
POLICY_REL="docs/security/fixtures/phase17-ai-artifact-lab/config/policy-config-v1.json"

command -v jq >/dev/null || {
    echo "REGRESSION_FAIL: jq unavailable"
    exit 1
}

SCRATCH="$(mktemp -d /tmp/phase21-regression.XXXXXX)"
trap 'rm -rf "$SCRATCH"' EXIT

# Export the complete committed security evidence tree because
# the Phase 17 verifier depends on the Phase 17 report, evidence,
# metadata, hashes, configuration, and fixture files.
git -C "$ROOT" archive HEAD docs/security |
    tar -xf - -C "$SCRATCH"

VERIFIER="$SCRATCH/$VERIFIER_REL"
POLICY="$SCRATCH/$POLICY_REL"
PHASE17_REPORT="$SCRATCH/docs/security/17-onyx-model-data-prompt-evaluation-ai-configuration-supply-chain.md"

test -f "$VERIFIER" || {
    echo "REGRESSION_FAIL: verifier absent"
    exit 1
}

test -f "$POLICY" || {
    echo "REGRESSION_FAIL: policy absent"
    exit 1
}

test -f "$PHASE17_REPORT" || {
    echo "REGRESSION_FAIL: Phase 17 report absent"
    exit 1
}

# ------------------------------------------------------------
# Baseline
# ------------------------------------------------------------

set +e
BASELINE_OUTPUT="$(
    cd "$SCRATCH"
    timeout 45s bash "$VERIFIER_REL" 2>&1
)"
BASELINE_RC=$?
set -e

printf '%s\n' "$BASELINE_OUTPUT"

if [ "$BASELINE_RC" -ne 0 ]; then
    echo "REGRESSION_FAIL: baseline verifier failed"
    exit 1
fi

printf '%s\n' "$BASELINE_OUTPUT" |
    grep -q 'core_pipeline_verification=PASS' || {
        echo "REGRESSION_FAIL: baseline PASS marker absent"
        exit 1
    }

# ------------------------------------------------------------
# Fail-closed mutation
# ------------------------------------------------------------

TMP_POLICY="${POLICY}.changed"

jq '.production_approved = true' \
    "$POLICY" > "$TMP_POLICY"

mv "$TMP_POLICY" "$POLICY"

set +e
MUTATED_OUTPUT="$(
    cd "$SCRATCH"
    timeout 45s bash "$VERIFIER_REL" 2>&1
)"
MUTATED_RC=$?
set -e

printf '%s\n' "$MUTATED_OUTPUT"

if [ "$MUTATED_RC" -eq 0 ]; then
    echo "REGRESSION_FAIL: invalid policy accepted"
    exit 1
fi

printf '%s\n' "$MUTATED_OUTPUT" |
    grep -q 'VERIFY_FAIL: policy approval' || {
        echo "REGRESSION_FAIL: expected rejection absent"
        exit 1
    }

echo "baseline_control=PASS"
echo "invalid_policy_rejected=PASS"
echo "original_repository_modified=NO"
echo "network_required=NO"
echo "phase21_verifier_regression=PASS"
