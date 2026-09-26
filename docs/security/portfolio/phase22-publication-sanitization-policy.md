# Phase 22 — Portfolio Publication and Sanitization Policy

## Purpose

Portfolio material must demonstrate real engineering capability without
exposing sensitive information or exaggerating the evidence.

## Default publication state

`NOT_REVIEWED`

Possible states:

- NOT_REVIEWED
- REVIEW_REQUIRED
- APPROVED_FOR_PUBLIC_PORTFOLIO
- PRIVATE_ONLY

## Required checks before publication

Public portfolio material must:

- contain no real passwords;
- contain no real authentication tokens;
- contain no private API keys;
- contain no private encryption material;
- contain no private customer data;
- contain no real confidential user records;
- contain no production secrets;
- contain no inappropriate private infrastructure identifiers;
- clearly label synthetic identities;
- clearly label synthetic credentials;
- clearly label synthetic incidents;
- preserve scope and authorization;
- preserve safety boundaries;
- preserve evidence provenance;
- preserve material limitations;
- distinguish observation from interpretation;
- distinguish testing from static review;
- distinguish findings from hypotheses;
- distinguish assisted work from independently reproduced work.

## Evidence integrity

Sanitization may remove sensitive content.

It must not materially change:

- what was tested;
- what was observed;
- what failed;
- what passed;
- how evidence was produced;
- known limitations.

## Security-testing publication rule

Public material must not require unauthorized testing of third-party or
production systems.

Demonstrations should use:

- local systems;
- synthetic data;
- bounded fixtures;
- authorized repositories;
- controlled environments.

## Employment-integrity rule

Résumé, GitHub, portfolio, freelance proposal and interview claims must
remain traceable to project evidence.

A task performed with substantial assistance must not be presented as
an independently reproduced task.

## Phase 21 limitation

Action 21.17 remains:

`BLOCKED_INDEPENDENT`

Therefore Phase 22 must not claim successful independent Phase 21
reproduction until that gate is actually passed.
