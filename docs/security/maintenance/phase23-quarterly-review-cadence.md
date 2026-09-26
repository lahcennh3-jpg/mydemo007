# Phase 23 — Quarterly Maintenance Cadence

## Purpose

The security project is no longer treated as a one-time assessment.

Relevant external and internal changes must trigger reassessment.

## Default quarterly cadence

Review windows:

- Q1 — January
- Q2 — April
- Q3 — July
- Q4 — October

A quarter does not need to wait for its normal review window when a
material security change occurs earlier.

## Quarterly review sequence

1. standards delta;
2. Onyx architecture delta;
3. Onyx release delta;
4. software dependency delta;
5. model delta;
6. dataset delta;
7. prompt delta;
8. authorization / tool / governance policy delta;
9. threat-model delta;
10. evaluation-set refresh;
11. detection refresh;
12. incident-response tabletop;
13. portfolio-evidence refresh;
14. unresolved-risk review;
15. publication / independence gate review.

## Required evidence

Each maintenance cycle should record:

- review timestamp;
- previous baseline;
- current baseline;
- observed changes;
- security relevance;
- affected assets;
- affected trust boundaries;
- affected threats;
- required tests;
- actual tests performed;
- evidence;
- remediation;
- regression state;
- residual risk;
- owner;
- next review trigger.

## No-change rule

"No material change" is a valid result only when the review itself is
recorded.

Absence of a review must not be represented as evidence that nothing
changed.

## Emergency trigger rule

A quarterly cadence does not override an urgent security trigger.

Examples include:

- significant upstream security advisory;
- material authorization change;
- new externally reachable interface;
- major RAG architecture change;
- agent/tool capability expansion;
- critical dependency change;
- model/provider change;
- new data class;
- confirmed security incident;
- material policy change.

## Provenance

Maintenance evidence must preserve its source, date, version and
relevant commit or artifact identity wherever available.
