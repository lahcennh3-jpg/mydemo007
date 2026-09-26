# Action 17.10 — Data-Poisoning Baseline

The controlled Phase-17 dataset gate checks:

- duplicate record identifiers
- extreme feature values outside the laboratory range
- invalid labels
- identical feature vectors with conflicting labels

The clean synthetic fixture passed.

The deliberately poisoned fixture was rejected.

These are baseline integrity heuristics.

They are not claimed to detect every form of training-data poisoning,
semantic poisoning, clean-label attack, backdoor, or distribution
manipulation.
