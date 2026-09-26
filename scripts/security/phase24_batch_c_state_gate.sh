#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ] || [ ! -r "$1" ]; then
  echo 'usage: phase24_batch_c_state_gate.sh STATE_FILE' >&2
  exit 2
fi

required=(EV007 EV008 EV009 EV011 EV012 EV013)
runtime=(EV005 EV006 EV010)
declare -A states=()
invalid=0

while IFS='=' read -r key state || [ -n "$key$state" ]; do
  case "$key" in
    EV005|EV006|EV007|EV008|EV009|EV010|EV011|EV012|EV013) ;;
    *) echo "UNKNOWN_STATE=$key" >&2; invalid=1; continue ;;
  esac

  if [ -n "${states[$key]+present}" ]; then
    echo "DUPLICATE_STATE=$key" >&2
    invalid=1
  fi

  case "$state" in
    PASS|FAIL|BLOCKED|INCONCLUSIVE) ;;
    *) echo "INVALID_STATE=$key" >&2; invalid=1 ;;
  esac
  states[$key]="$state"
done < "$1"

for key in "${required[@]}"; do
  if [ "${states[$key]-MISSING}" != PASS ]; then
    echo "REQUIRED_CONTROL=$key:${states[$key]-MISSING}" >&2
    invalid=1
  fi
done

full_evaluation=PASS
for key in "${runtime[@]}"; do
  case "${states[$key]-MISSING}" in
    PASS) ;;
    BLOCKED) full_evaluation=BLOCKED ;;
    *) echo "RUNTIME_EVALUATION=$key:${states[$key]-MISSING}" >&2; invalid=1 ;;
  esac
done

if [ "$invalid" -ne 0 ]; then
  echo 'BATCH_C_CONTROL_GATE=FAIL'
  exit 1
fi

echo 'BATCH_C_CONTROL_GATE=PASS'
echo "BATCH_C_FULL_EVALUATION=$full_evaluation"
