#!/bin/sh
set -eu

PROMPT="${1:-}"

case "$PROMPT" in
    *phase14-block*)
        printf '%s\n' \
          "PHASE14_BLOCKED"
        ;;
    *)
        printf '%s\n' \
          "PHASE14_SAFE"
        ;;
esac
