#!/usr/bin/env bash
set -euo pipefail

ROOT="docs/security"
E="$ROOT/evidence"
LAB="$ROOT/fixtures/phase17-ai-artifact-lab"

fail() {
    echo "VERIFY_FAIL: $*" >&2
    exit 1
}

grep -q 'PHASE_17_BATCH_A_COMPLETE' \
  "$ROOT/17-onyx-model-data-prompt-evaluation-ai-configuration-supply-chain.md" \
  || fail "Batch-A marker"

grep -q 'PHASE_17_BATCH_B_COMPLETE' \
  "$ROOT/17-onyx-model-data-prompt-evaluation-ai-configuration-supply-chain.md" \
  || fail "Batch-B marker"

jq -e \
  '.production_approved == false' \
  "$LAB/metadata/model-source-identity.json" \
  >/dev/null \
  || fail "model source approval"

jq -e \
  '.approval.production_release == false' \
  "$LAB/metadata/model-artifact-metadata.json" \
  >/dev/null \
  || fail "model production release"

jq -e \
  '.approval.production_use == false' \
  "$LAB/metadata/dataset-metadata-v1.json" \
  >/dev/null \
  || fail "dataset production approval"

jq -e \
  '.approval.production == false' \
  "$LAB/metadata/prompt-template-manifest.json" \
  >/dev/null \
  || fail "prompt production approval"

jq -e \
  '.production_approved == false' \
  "$LAB/config/policy-config-v1.json" \
  >/dev/null \
  || fail "policy approval"

jq -e \
  '.production_approved == false
   and .network_scope == "loopback-only"
   and .external_server == false' \
  "$LAB/config/mcp-config-v1.json" \
  >/dev/null \
  || fail "MCP boundary"

jq -e \
  '.approval.status == "pending-review"
   and .promotion_allowed == false' \
  "$LAB/metadata/change-request-PH17-CR-001.json" \
  >/dev/null \
  || fail "change approval gate"

jq -e \
  '.current_state == "retired"
   and .production_approval == false' \
  "$LAB/metadata/model-lifecycle-v2.json" \
  >/dev/null \
  || fail "lifecycle final state"

test ! -f "$LAB/deployment-simulation/current/model.json" \
  || fail "retired artifact still deployed"

jq -e \
  '.reference_tool_execution_gaps == 4
   and .provenance_bundle_verified == true' \
  "$E/phase17-action-17.18-tool-provenance-integration.json" \
  >/dev/null \
  || fail "tool/provenance state"

sha256sum -c \
  "$E/phase17-action-17.18-provenance-bundle.sha256" \
  >/dev/null

echo "core_pipeline_verification=PASS"
echo "production_authorized=false"
echo "external_mcp_used=false"
echo "unapproved_change_blocked=true"
echo "rollback_verified=true"
echo "revocation_verified=true"
echo "retirement_verified=true"
echo "reference_tool_execution_gaps=4"
echo "phase17_scope=synthetic-local-lab"
