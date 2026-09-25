# Phase 15 — Synthetic Incident Lessons Learned

## Incident

`INC-P15-001`

## What worked

- cross-tenant authorization attempt was detected;
- prompt-injection signal correlated to the later tool call;
- retrieval tenant/provenance anomaly was detected;
- unapproved security configuration change was detected;
- unexpected runtime destination was detected;
- excessive resource activity was detected;
- no prohibited raw sensitive event fields were required;
- evidence could be reconstructed from identifiers and hashes.

## Preventive improvements

1. Keep tenant identity on authorization and retrieval events.
2. Preserve trace correlation across prompt, agent and tool events.
3. Version and hash model, prompt, policy and configuration state.
4. Preserve approval identifiers for sensitive actions.
5. Maintain runtime destination allowlists.
6. Alert on provenance and tenant mismatch.
7. Keep quotas, cancellation and economic controls observable.
8. Reject telemetry missing mandatory correlation fields.
9. Reject prohibited sensitive logging fields.
10. Convert every confirmed incident pattern into regression coverage.

## Detection-engineering lessons

Synthetic perfect precision and recall do not imply production performance.

Production baselines would require real deployment telemetry, representative
traffic, tuning, alert review and measured false-positive/false-negative rates.

## Result

`LESSONS_LEARNED_COMPLETE`
