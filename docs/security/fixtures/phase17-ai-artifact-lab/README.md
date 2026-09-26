# Phase 17 Synthetic AI Artifact Laboratory

Purpose:

- AI artifact supply-chain security testing
- synthetic data and artifacts only
- no production models
- no real customer data
- no real credentials
- no external AI APIs
- no unsafe pickle loading
- no deployment of quarantined artifacts

Trust flow:

synthetic source
    |
    v
source/
    |
    v
quarantine/
    |
    +--> provenance verification
    +--> hash verification
    +--> serialization inspection
    +--> format analysis
    |
    v
approved/

An artifact MUST NOT move from quarantine to approved unless its
required verification gates pass.

This Phase-17 lab is intentionally separate from production Onyx
model artifacts and production model-serving infrastructure.
