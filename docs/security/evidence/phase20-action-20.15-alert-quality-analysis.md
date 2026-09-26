# Phase 20 — Alert Quality and Error Analysis

## Positive controls

All twelve deliberately represented synthetic detection conditions must be
detected.

## Negative controls

Allowed synthetic operations include:

- successful authentication;
- authorized conversation access;
- authorized RAG retrieval;
- authorized tool invocation.

These must remain allowed and must not be transformed into denial detections.

## Threshold boundary

The threshold of three events used for repeated authentication failure and
repeated resource-limit violations is a deterministic laboratory threshold.

It is not a recommended production threshold.

## Production limits

This laboratory does not establish:

- production precision;
- production recall;
- production base rates;
- production alert volume;
- analyst workload;
- production false-positive rate;
- production false-negative rate;
- production detection latency.
