#!/usr/bin/env bash
set -euo pipefail

FILE="${1:?dataset required}"

awk -F',' '
BEGIN {
    findings = 0
}

NR == 1 {
    if ($0 != "id,x1,x2,x3,label") {
        print "FINDING invalid_header"
        findings++
    }
    next
}

{
    id = $1
    x1 = $2 + 0
    x2 = $3 + 0
    x3 = $4 + 0
    label = $5

    if (seen_id[id]++) {
        print "FINDING duplicate_id id=" id
        findings++
    }

    if (x1 < -5 || x1 > 5 ||
        x2 < -5 || x2 > 5 ||
        x3 < -5 || x3 > 5) {

        print "FINDING feature_out_of_expected_range id=" id
        findings++
    }

    if (label != "0" && label != "1") {
        print "FINDING invalid_label id=" id " label=" label
        findings++
    }

    feature_key = $2 "," $3 "," $4

    if (feature_key in feature_label &&
        feature_label[feature_key] != label) {

        print "FINDING conflicting_label feature_vector=" feature_key
        findings++
    }

    feature_label[feature_key] = label
}

END {
    print "finding_count=" findings

    if (findings > 0) {
        exit 2
    }
}
' "$FILE"
