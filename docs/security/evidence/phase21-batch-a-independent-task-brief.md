# Phase 21 Batch A — Independent Practice Brief

## Objective

Demonstrate that the previous security work can be independently rebuilt,
reproduced, explained, transferred, and reviewed.

This batch covers Actions 21.1–21.7.

## Independence rule

The engineer performs the actual rebuild and reproduction commands from
understanding rather than copying a previous command sequence.

Permitted references:

- source code;
- command `--help`;
- local documentation;
- man pages;
- architecture/evidence created during earlier phases;
- official documentation when needed.

The evidence must not claim that command provenance can be technically proven.
A terminal transcript proves execution, not whether text was manually typed.

## Safety boundary

Only the authorized local/synthetic environment may be used.

Do not use:

- production deployments;
- customer data;
- real credentials;
- public targets;
- real external AI APIs;
- unbounded load tests.

Stop on:

- unexpected external network activity;
- real secrets or real personal data;
- ambiguous authorization;
- uncontrolled resource consumption.

## Action 21.1

Rebuild the authorized Onyx lab from the clean Phase-20 source snapshot.

Required evidence:

- clean source identity;
- environment prerequisites;
- rebuild decisions;
- runtime components started;
- health verification;
- failure signals;
- teardown/rollback procedure;
- limitations.

## Action 21.2

Independently reproduce representative findings or controls from earlier
security phases.

Use representative examples across multiple security domains where practical.

For each reproduction record:

- original finding/control;
- prediction;
- self-derived procedure;
- observed result;
- evidence;
- interpretation;
- whether the old conclusion still holds;
- limitations.

## Action 21.3

For important commands used in 21.1 and 21.2 explain:

- purpose;
- execution target;
- expected effect;
- evidence produced;
- failure signal;
- rollback.

## Action 21.4

Transfer one already-learned security method to an unfamiliar application
from the set of already-completed supporting projects.

Do not add a new project solely to satisfy Phase 21.

Record:

- transferred method;
- assumptions;
- architecture differences;
- adaptations;
- prediction;
- observation;
- result;
- transfer limitations.

## Action 21.5

Perform a security code review.

Inspect relevant:

- trust boundaries;
- authentication;
- authorization;
- tenant ownership;
- input validation;
- output handling;
- data access;
- secrets;
- logging;
- error handling;
- dependencies;
- AI-specific control paths.

Every finding must contain source evidence and an explicit confidence level.

## Action 21.6

Perform an architecture review.

Cover:

- components;
- trust boundaries;
- identities;
- data stores;
- AI/model boundaries;
- retrieval;
- agents/tools/MCP where applicable;
- external interfaces;
- privileged flows;
- failure modes;
- detection points;
- recovery paths.

## Action 21.7

Perform a design review.

For one security-sensitive workflow document:

- security objective;
- assumptions;
- misuse cases;
- trust decisions;
- authorization point;
- validation point;
- least privilege;
- failure behavior;
- observability;
- rollback;
- alternatives considered;
- residual risk.

## Batch-A completion rule

21.1–21.7 are not COMPLETE merely because these templates exist.

Each action becomes COMPLETE only after its corresponding evidence has been
performed, written, and validated.
