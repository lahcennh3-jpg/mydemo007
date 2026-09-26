# Residual assurance reconciliation

The Phase 25 handoff lists twelve open risks. It omits ten open requirements
from the Phase 9 and Phase 16 closeouts.

The [consolidated register](phase25-consolidated-residual-assurance.tsv)
lists all 22 items. No row means that a production risk was accepted.
The twelve Phase 25 dates remain as recorded. Dates for the older ten items
are unset. The project owner must assign dates and deployment owners before
a production release decision.

Sources:

- [Phase 25 handoff](phase25-residual-risk-handoff.tsv): R24-001 to R24-012.
- [Phase 9 closeout](../evidence/phase9-action-9.14-final-completion-gate.md):
  R9-01 to R9-06.
- [Phase 16 closeout](../16-onyx-secure-software-container-configuration-supply-chain.md):
  four outstanding production assurance requirements.

R9-05 requires the full supported test environment. The Phase 24 gate CI
checks one control runner and does not close R9-05.
R16-03 requires an approved production trust chain. The Phase 16 local signing
demonstration does not close R16-03.
R24-006 requires source and image correspondence. Matching an image to the
Phase 24 image baseline does not close R24-006.

This register records later reconciliation. It does not rewrite the
historical Phase 25 completion decision or the original evidence counts.
