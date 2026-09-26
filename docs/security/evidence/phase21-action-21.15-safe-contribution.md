# Phase 21 — Action 21.15 — Safe Contribution

## Contribution

A bounded regression test was added for the Phase 17 approval verifier.

Path:

`docs/security/fixtures/phase21/test-phase17-verifier-regression.sh`

## Repair history

The initial attempt exported only the Phase 17 fixture directory and therefore
omitted verifier dependencies elsewhere under `docs/security`.

The second attempt corrected the archive scope, proving that the baseline
verifier passes, but the mutation step depended on unavailable `python3`.

The final version uses the existing `jq` dependency instead.

## Security properties

1. Valid committed baseline must pass.
2. Synthetic `production_approved=true` must fail closed.
3. Mutation occurs only inside a temporary archive.
4. Repository source remains unchanged.

## Validation

- complete security-tree export: PASS
- baseline verifier: PASS
- invalid policy rejected: PASS
- repository mutation: NO
- outbound network required by regression test: NO
- test exit: 0
- SHA-256: `ff913c0be10d4f220a4ec940234172b55331ae8e299d10b2505d0e3f7e1b6760`

CONTRIBUTION_TYPE=TEST_HARDENING
REPAIR_1=FULL_DOCS_SECURITY_EXPORT
REPAIR_2=REMOVE_UNAVAILABLE_PYTHON3_DEPENDENCY
ACTION_RESULT=PASS_SAFE_REPOSITORY_CONTRIBUTION
