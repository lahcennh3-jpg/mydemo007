# Phase 21 — Action 21.12 — Engineering Trade-off

Status: ASSISTED_DRAFT

## Decision

Preserve the Phase 21 rebuild blocker instead of weakening the acceptance
criteria to obtain an artificial PASS.

## Trade-off

This slows formal phase completion but preserves evidence integrity.

## Rejected shortcut

Treating source-level tests or an earlier working deployment as equivalent
to a clean independent rebuild.

## Reason

A professional security assessment must distinguish:

- verified behavior,
- inherited evidence,
- assisted reproduction,
- independent reproduction,
- environment limitations.

## Rollback

No product/runtime change was required for this decision.

ACTION_RESULT=ASSISTED_DRAFT
