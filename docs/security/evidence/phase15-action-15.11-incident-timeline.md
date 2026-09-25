# Phase 15 — Synthetic Incident Timeline

Incident: `INC-P15-001`

This is a synthetic local security exercise.

| Timestamp | Event | Type | Result | Detection |
| --- | --- | --- | --- | --- |
| 2026-01-15T14:00:00Z | INC15-E001 | prompt_security_signal | blocked | correlation signal / no direct alert |
| 2026-01-15T14:00:01Z | INC15-E002 | tool_call | blocked | D15-003 |
| 2026-01-15T14:01:00Z | INC15-E003 | authorization_decision | deny | D15-001 |
| 2026-01-15T14:02:00Z | INC15-E004 | retrieval | blocked | D15-005 |
| 2026-01-15T14:03:00Z | INC15-E005 | configuration_change | blocked | D15-007 |
| 2026-01-15T14:04:00Z | INC15-E006 | runtime_destination | blocked | D15-004 |
| 2026-01-15T14:05:00Z | INC15-E007 | resource_usage | cancelled | D15-009 |
