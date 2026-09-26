# Phase 23 — Continuous 2026+ Maintenance and Optional Specialization

## Purpose

Maintain the security-engineering body of work after completion of the
core roadmap rather than treating it as permanently current.

## Source checkpoint

Source branch:

`security/phase-22-final-portfolio-employment-readiness`

Source commit:

`aadc9801593811f89670ea6b8a58bef4ac3c95b6`

## Inherited Phase 22 state

PHASE22_WORKFLOW_COMPLETE=YES

PHASE22_COMPLETE=YES_WITH_LIMITATIONS

EMPLOYMENT_PRESENTATION_READY=YES_WITH_LIMITATIONS

PUBLICATION_APPROVED=NO

INDEPENDENT_PROJECT_COMPLETION=NO

ACTION_21.17=BLOCKED_INDEPENDENT

PHASE21_COMPLETE=NO

## Phase 23 maintenance domains

- AI security standards;
- Onyx architecture;
- Onyx releases;
- software dependencies;
- models;
- datasets;
- prompts;
- authorization/tool/governance policies;
- threat models;
- evaluation sets;
- detections;
- incident-response tabletops;
- portfolio evidence.

## Default cadence

Quarterly, plus event-driven review after material security changes.

## Optional specialization

Current state:

`DEFERRED_UNTIL_CAPSTONE_PROMOTION_GATE`

Continuous maintenance may proceed despite that specialization gate.

## Batch A

Batch A establishes the Phase 23 maintenance control plane.

PHASE23_BATCH_A=READY_FOR_VERIFICATION

PHASE23_COMPLETE=NO

## Batch B — 2026 Q3 standards and Onyx technical refresh

Review timestamp UTC:

`2026-09-26T13:41:31Z`

Batch B refreshed:

- NIST AI-risk-management references;
- NIST SSDF AI profile;
- OWASP LLM Top 10 2026;
- OWASP Agentic Applications Top 10 2026;
- OWASP Agent Control Standard;
- OWASP ASVS;
- Onyx current upstream release metadata;
- Onyx baseline-to-current technical delta metadata;
- security regression-selection decisions.

Protected Onyx baseline:

`160f9b143605ca45a85bd387b5bd173840bab15d`

Current upstream tag observed:

`v4.8.1`

No automatic baseline upgrade was performed.

ACTION_23.6=PASS_BATCH_A_HANDOFF_GATE

ACTION_23.7=PASS_CURRENT_STANDARDS_REFRESH

ACTION_23.8=PASS_ONYX_UPSTREAM_TECHNICAL_REFRESH

ACTION_23.9=PASS_SECURITY_DELTA_TRIAGE

ACTION_23.10=READY_FOR_FINAL_VERIFICATION

PHASE23_BATCH_B=READY_FOR_VERIFICATION

PHASE23_COMPLETE=NO

NEXT=BATCH_C_AI_RUNTIME_DATA_POLICY_THREAT_EVALUATION_REFRESH
