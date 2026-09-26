#!/usr/bin/env bash
set -euo pipefail

gate="$(dirname "${BASH_SOURCE[0]}")/phase24_batch_c_state_gate.sh"
fixture="$(mktemp)"
trap 'rm -f "$fixture"' EXIT

write_fixture() {
  cat > "$fixture" <<'STATES'
EV005=BLOCKED
EV006=BLOCKED
EV007=PASS
EV008=PASS
EV009=PASS
EV010=BLOCKED
EV011=PASS
EV012=PASS
EV013=PASS
STATES
}

must_fail() {
  if bash "$gate" "$fixture" > /dev/null 2>&1; then
    echo "Expected failure: $1" >&2
    exit 1
  fi
}

write_fixture
result="$(bash "$gate" "$fixture")"
[[ "$result" == *'BATCH_C_CONTROL_GATE=PASS'* ]]
[[ "$result" == *'BATCH_C_FULL_EVALUATION=BLOCKED'* ]]

write_fixture
sed -i 's/EV007=PASS/EV007=FAIL/' "$fixture"
must_fail 'failed required control'

write_fixture
sed -i 's/EV009=PASS/EV009=INCONCLUSIVE/' "$fixture"
must_fail 'inconclusive required control'

write_fixture
sed -i '/^EV012=/d' "$fixture"
must_fail 'missing required control'

write_fixture
echo 'EV011=PASS' >> "$fixture"
must_fail 'duplicate control'

write_fixture
sed -i 's/EV005=BLOCKED/EV005=FAIL/' "$fixture"
must_fail 'failed runtime evaluation'

write_fixture
sed -i 's/EV010=BLOCKED/EV010=PASS/' "$fixture"
result="$(bash "$gate" "$fixture")"
[[ "$result" == *'BATCH_C_FULL_EVALUATION=BLOCKED'* ]]

write_fixture
sed -i 's/=BLOCKED/=PASS/g' "$fixture"
result="$(bash "$gate" "$fixture")"
[[ "$result" == *'BATCH_C_FULL_EVALUATION=PASS'* ]]

echo 'BATCH_C_STATE_GATE_TEST=PASS'
