# Phase 24 — Batch B BOLA Retest

Timestamp UTC: 2026-09-26T16:59:26Z

SOURCE_HEAD=3867f13e055b56cb313ccc7070a5ed6955efd653

RUNNER_SHA256=88874f3a81ad4b20f97ee90956c138d95a87e6a2112fa02fd8410cc2de2ead3e

NETWORK_SCOPE=INTERNAL_ONLY

RETEST_CLIENT_EXTERNAL_NETWORK=DENIED

SYNTHETIC_IDENTITIES_ONLY=YES

RAW_RESPONSE_BODIES_STORED=NO

PASSWORDS_STORED=NO

## Original result

EV23-002_ORIGINAL=INCONCLUSIVE

ORIGINAL_AMBIGUOUS_CASE=BOLA-004

ORIGINAL_NON_OWNER_DELETE_HTTP_STATUS=400

ORIGINAL_UNAUTHORIZED_DELETE_EFFECT_OBSERVED=NO

The HTTP 400 response from the delete route was not reclassified as a
security PASS or security FAIL.

## Retest design

The retest uses the product's existing stop-chat-session ownership contract
with positive and negative controls against the same synthetic object.

Cases:

- owner creates session;
- owner reads session;
- non-owner read denied;
- non-owner stop denied;
- owner stop accepted on same route and same object;
- owner remains able to retrieve session afterward.

## Result

RETEST_CASES=6

RETEST_PASS_CASES=6

RETEST_FAIL_CASES=0

EV23-002_RETEST=PASS

BOLA_DELETE_400_REMAINS_ROUTE_SEMANTICS_LIMITATION=YES

ACTION_24.10R=PASS

CURRENT_RUNTIME_REGRESSION_COMPLETE=NO
