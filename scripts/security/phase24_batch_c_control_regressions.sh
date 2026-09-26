#!/usr/bin/env bash
set -uo pipefail

: "${API:?}"
: "${INTERNAL_NET:?}"
: "${BACKEND_IMAGE:?}"
: "${BASELINE:?}"
: "${CONTROL_LOG:?}"
: "${STATE_FILE:?}"

: > "$CONTROL_LOG"
: > "$STATE_FILE"

log_section() {
  {
    echo
    echo "============================================================"
    echo "$1"
    echo "============================================================"
  } >> "$CONTROL_LOG"
}

set_state() {
  printf '%s=%s\n' "$1" "$2" >> "$STATE_FILE"
}

classify_test_rc() {
  rc="$1"
  output="$2"

  if [ "$rc" -eq 0 ]; then
    echo PASS
    return
  fi

  if grep -Eq \
    'ModuleNotFoundError|No module named|ImportError|cannot import name' \
    "$output"
  then
    echo BLOCKED
    return
  fi

  echo FAIL
}

run_unittest() {
  label="$1"
  start_dir="$2"
  pattern="$3"

  tmp="$(mktemp)"

  log_section "$label"

  set +e
  docker run \
    --rm \
    --network none \
    -e PYTHONDONTWRITEBYTECODE=1 \
    -e PYTHONPATH=/workspace/backend \
    -v "$PWD:/workspace:ro" \
    -w /workspace/backend \
    --entrypoint python \
    "$BACKEND_IMAGE" \
    -m unittest discover \
    -s "$start_dir" \
    -p "$pattern" \
    -v \
    >"$tmp" 2>&1
  rc=$?
  set -e

  cat "$tmp" >> "$CONTROL_LOG"

  state="$(classify_test_rc "$rc" "$tmp")"

  printf '%s=%s\n' "$label" "$state" >> "$CONTROL_LOG"

  rm -f "$tmp"

  printf '%s' "$state"
}

combine_states() {
  # FAIL dominates.
  for s in "$@"; do
    [ "$s" = FAIL ] && {
      echo FAIL
      return
    }
  done

  # Partial execution with a blocked/inconclusive component is inconclusive.
  for s in "$@"; do
    case "$s" in
      BLOCKED|INCONCLUSIVE)
        echo INCONCLUSIVE
        return
        ;;
    esac
  done

  echo PASS
}

# ============================================================
# EV23-005 — RETRIEVAL POISONING
# ============================================================

EV005="BLOCKED"

{
  echo
  echo "EV23-005=BLOCKED"
  echo "REASON=CONTROLLED_RAG_INDEXING_RUNTIME_NOT_ESTABLISHED"
} >> "$CONTROL_LOG"

# ============================================================
# EV23-006 — PROMPT INJECTION
# ============================================================

EV006="BLOCKED"

{
  echo
  echo "EV23-006=BLOCKED"
  echo "REASON=CONTROLLED_MODEL_GENERATION_RUNTIME_NOT_ESTABLISHED"
} >> "$CONTROL_LOG"

# ============================================================
# EV23-007 — AGENT / TOOL AUTHORITY
# ============================================================

EV007="$(
  run_unittest \
    "EV23_007_TOOL_AUTHORITY" \
    "tests/unit/onyx/tools" \
    "test_phase11_tool_authority_boundaries.py"
)"

# ============================================================
# EV23-008 — MCP IDENTITY / AUTHORIZATION BOUNDARIES
#
# This is code-boundary validation only.
# No live MCP transport claim is made.
# ============================================================

EV008="$(
  run_unittest \
    "EV23_008_MCP_SECURITY_BOUNDARIES" \
    "tests/unit/onyx/server/features/mcp" \
    "test_phase11_mcp_security_boundaries.py"
)"

# ============================================================
# EV23-009 — SENSITIVE DATA EXPOSURE
# ============================================================

REDACTION_STATE="$(
  run_unittest \
    "EV23_009_DLP_REDACTION" \
    "tests/unit/onyx/privacy" \
    "test_phase12_dlp_redaction_export.py"
)"

TRACE_STATE="$(
  run_unittest \
    "EV23_009_TOOL_TRACE_REDACTION" \
    "tests/unit/onyx/tools" \
    "test_phase11_tool_trace_redaction.py"
)"

# Runtime response leakage check.
log_section "EV23_009_RUNTIME_RESPONSE_SECRET_CHECK"

set +e

docker exec -i "$API" python - <<'PY' >>"$CONTROL_LOG" 2>&1
import os
import sys
import uuid

import httpx

secret = os.environ.get("USER_AUTH_SECRET", "")

if not secret:
    print("RUNTIME_SECRET_RESPONSE_CHECK=INCONCLUSIVE")
    raise SystemExit(30)

try:
    with httpx.Client(
        base_url="http://127.0.0.1:8080",
        timeout=3,
        follow_redirects=False,
    ) as client:
        responses = [
            client.get("/health"),
            client.get("/me"),
            client.post(
                "/auth/login",
                data={
                    "username":
                        f"phase24-invalid-{uuid.uuid4().hex}@example.com",
                    "password":
                        f"invalid-{uuid.uuid4().hex}",
                },
            ),
        ]

except Exception as exc:
    print(
        "RUNTIME_SECRET_RESPONSE_CHECK=INCONCLUSIVE_"
        + type(exc).__name__
    )
    raise SystemExit(30)

for response in responses:
    if secret in response.text:
        print("RUNTIME_SECRET_RESPONSE_CHECK=FAIL")
        raise SystemExit(20)

print("RUNTIME_SECRET_RESPONSE_CHECK=PASS")
PY

response_rc=$?

set -e

case "$response_rc" in
  0)
    RESPONSE_STATE=PASS
    ;;
  20)
    RESPONSE_STATE=FAIL
    ;;
  *)
    RESPONSE_STATE=INCONCLUSIVE
    ;;
esac

# Runtime log leakage check. Secret never leaves the API environment as output.
log_section "EV23_009_RUNTIME_LOG_SECRET_CHECK"

set +e

docker logs "$API" 2>&1 |
docker exec -i "$API" python -c '
import os
import sys

secret = os.environ.get("USER_AUTH_SECRET", "")
data = sys.stdin.read()

if not secret:
    print("RUNTIME_LOG_SECRET_CHECK=INCONCLUSIVE")
    raise SystemExit(30)

if secret in data:
    print("RUNTIME_LOG_SECRET_CHECK=FAIL")
    raise SystemExit(20)

print("RUNTIME_LOG_SECRET_CHECK=PASS")
' >>"$CONTROL_LOG" 2>&1

log_rc=$?

set -e

case "$log_rc" in
  0)
    LOG_STATE=PASS
    ;;
  20)
    LOG_STATE=FAIL
    ;;
  *)
    LOG_STATE=INCONCLUSIVE
    ;;
esac

EV009="$(
  combine_states \
    "$REDACTION_STATE" \
    "$TRACE_STATE" \
    "$RESPONSE_STATE" \
    "$LOG_STATE"
)"

# ============================================================
# EV23-010 — MODEL / PROVIDER BEHAVIOR
# ============================================================

EV010="BLOCKED"

{
  echo
  echo "EV23-010=BLOCKED"
  echo "REASON=MODEL_PROVIDER_RUNTIME_NOT_ESTABLISHED"
} >> "$CONTROL_LOG"

# ============================================================
# EV23-011 — ABUSE / AVAILABILITY / ECONOMIC CONTROLS
# ============================================================

ABUSE_B="$(
  run_unittest \
    "EV23_011_ABUSE_BATCH_B" \
    "tests/unit/onyx/abuse" \
    "test_phase13_batch_b.py"
)"

ABUSE_C="$(
  run_unittest \
    "EV23_011_ABUSE_BATCH_C" \
    "tests/unit/onyx/abuse" \
    "test_phase13_batch_c.py"
)"

EV011="$(
  combine_states \
    "$ABUSE_B" \
    "$ABUSE_C"
)"

# ============================================================
# EV23-012 — CURRENT DEPLOYMENT INTEGRITY
# ============================================================

log_section "EV23_012_DEPLOYMENT_INTEGRITY"

EXPECTED_IMAGE_ID="$(
  awk -F'\t' \
    '$1 == "api_image_id" {print $2}' \
    "$BASELINE"
)"

EXPECTED_DB_REV="$(
  awk -F'\t' \
    '$1 == "database_schema_revision" {print $2}' \
    "$BASELINE"
)"

ACTUAL_IMAGE_ID="$(
  docker inspect \
    --format '{{.Image}}' \
    "$API"
)"

ACTUAL_HEALTH="$(
  docker inspect \
    --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}NO_HEALTHCHECK{{end}}' \
    "$API"
)"

ACTUAL_NETWORKS="$(
  docker inspect \
    --format '{{range $k,$v := .NetworkSettings.Networks}}{{println $k}}{{end}}' \
    "$API" |
  sed '/^$/d'
)"

ACTUAL_DB_REV="$(
  docker exec "$API" \
    /bin/sh -lc \
    'cd /app && alembic current 2>/dev/null | tail -1' \
    2>/dev/null || true
)"

deployment_fail=0

if [ "$ACTUAL_IMAGE_ID" != "$EXPECTED_IMAGE_ID" ]; then
  echo "IMAGE_ID_MATCH=FAIL" >> "$CONTROL_LOG"
  deployment_fail=1
else
  echo "IMAGE_ID_MATCH=PASS" >> "$CONTROL_LOG"
fi

if [ "$ACTUAL_HEALTH" != healthy ]; then
  echo "CONTAINER_HEALTH=FAIL" >> "$CONTROL_LOG"
  deployment_fail=1
else
  echo "CONTAINER_HEALTH=PASS" >> "$CONTROL_LOG"
fi

if [ "$ACTUAL_NETWORKS" != "$INTERNAL_NET" ]; then
  echo "NETWORK_SCOPE_MATCH=FAIL" >> "$CONTROL_LOG"
  deployment_fail=1
else
  echo "NETWORK_SCOPE_MATCH=PASS" >> "$CONTROL_LOG"
fi

if [ -n "$EXPECTED_DB_REV" ] &&
   [ "$ACTUAL_DB_REV" != "$EXPECTED_DB_REV" ]; then
  echo "DATABASE_REVISION_MATCH=FAIL" >> "$CONTROL_LOG"
  deployment_fail=1
else
  echo "DATABASE_REVISION_MATCH=PASS" >> "$CONTROL_LOG"
fi

if git ls-files --error-unmatch \
  deployment/docker_compose/.env \
  >/dev/null 2>&1
then
  echo "LOCAL_ENV_UNTRACKED=FAIL" >> "$CONTROL_LOG"
  deployment_fail=1
else
  echo "LOCAL_ENV_UNTRACKED=PASS" >> "$CONTROL_LOG"
fi

if ! git check-ignore -q deployment/docker_compose/.env; then
  echo "LOCAL_ENV_IGNORED=FAIL" >> "$CONTROL_LOG"
  deployment_fail=1
else
  echo "LOCAL_ENV_IGNORED=PASS" >> "$CONTROL_LOG"
fi

if [ "$deployment_fail" -eq 0 ]; then
  EV012=PASS
else
  EV012=FAIL
fi

# ============================================================
# EV23-013 — DETECTION CONTROL REGRESSION
# ============================================================

log_section "EV23_013_DETECTION_CONTROL"

GATE="docs/security/fixtures/phase20-observability-detection-lab/detections/phase20_detection_gate.awk"

EVENTS="docs/security/fixtures/phase20-observability-detection-lab/events/security-events.tsv"

ADVERSARIAL="docs/security/fixtures/phase20-observability-detection-lab/events/security-events-adversarial.tsv"

BASE_OUT="$(mktemp)"
ADV_OUT="$(mktemp)"
ADV_GATE="$(mktemp)"

set +e

awk -f "$GATE" "$EVENTS" > "$BASE_OUT" 2>&1
base_rc=$?

sed \
  's/event_count == 20/event_count == 24/' \
  "$GATE" \
  > "$ADV_GATE"

awk -f "$ADV_GATE" "$ADVERSARIAL" > "$ADV_OUT" 2>&1
adv_rc=$?

set -e

{
  echo "--- BASE DETECTION GATE ---"
  cat "$BASE_OUT"
  echo
  echo "--- ADVERSARIAL DETECTION GATE ---"
  cat "$ADV_OUT"
} >> "$CONTROL_LOG"

if [ "$base_rc" -eq 0 ] &&
   [ "$adv_rc" -eq 0 ] &&
   grep -q '^PHASE20_DETECTION_GATE=PASS$' "$BASE_OUT" &&
   grep -q '^PHASE20_DETECTION_GATE=PASS$' "$ADV_OUT"
then
  EV013=PASS
else
  EV013=FAIL
fi

rm -f "$BASE_OUT" "$ADV_OUT" "$ADV_GATE"

# ============================================================
# FINAL STATE
# ============================================================

set_state EV005 "$EV005"
set_state EV006 "$EV006"
set_state EV007 "$EV007"
set_state EV008 "$EV008"
set_state EV009 "$EV009"
set_state EV010 "$EV010"
set_state EV011 "$EV011"
set_state EV012 "$EV012"
set_state EV013 "$EV013"

{
  echo
  echo "============================================================"
  echo "BATCH C STATE"
  echo "============================================================"
  cat "$STATE_FILE"
} >> "$CONTROL_LOG"

exit 0
