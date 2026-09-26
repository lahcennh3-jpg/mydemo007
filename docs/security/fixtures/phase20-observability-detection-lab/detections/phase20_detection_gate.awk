BEGIN {
    FS = "\t"

    expected["REPEATED_AUTH_FAILURE"] = 1
    expected["WORKLOAD_IDENTITY_FAILURE"] = 1
    expected["CROSS_USER_ACCESS"] = 1
    expected["CROSS_TENANT_ACCESS"] = 1
    expected["UNAUTHORIZED_RAG_RETRIEVAL"] = 1
    expected["UNAUTHORIZED_MEMORY_ACCESS"] = 1
    expected["AGENT_POLICY_DENIAL"] = 1
    expected["TOOL_AUTHORIZATION_DENIAL"] = 1
    expected["MCP_POLICY_DENIAL"] = 1
    expected["SENSITIVE_EXPORT_DENIAL"] = 1
    expected["REPEATED_RESOURCE_VIOLATION"] = 1
    expected["WORKLOAD_PRIVILEGE_DENIAL"] = 1
}

NR == 1 {
    if ($1 != "EVENT_ID" ||
        $2 != "DOMAIN" ||
        $3 != "ACTOR" ||
        $4 != "TENANT" ||
        $5 != "RESOURCE" ||
        $6 != "ACTION" ||
        $7 != "OUTCOME" ||
        $8 != "CONTROL") {
        print "SCHEMA_VALIDATION=FAIL"
        exit 2
    }

    next
}

NF {
    event_count++

    domain = $2
    actor = $3
    outcome = $7
    control = $8

    if (domain == "authentication" && outcome == "DENIED")
        auth_fail[actor]++

    if (domain == "identity" && outcome == "DENIED")
        actual["WORKLOAD_IDENTITY_FAILURE"] = 1

    if (control == "CROSS_USER" && outcome == "DENIED")
        actual["CROSS_USER_ACCESS"] = 1

    if (control == "CROSS_TENANT" && outcome == "DENIED")
        actual["CROSS_TENANT_ACCESS"] = 1

    if (control == "RAG_AUTHZ" && outcome == "DENIED")
        actual["UNAUTHORIZED_RAG_RETRIEVAL"] = 1

    if (control == "MEMORY_AUTHZ" && outcome == "DENIED")
        actual["UNAUTHORIZED_MEMORY_ACCESS"] = 1

    if (control == "AGENT_POLICY" && outcome == "DENIED")
        actual["AGENT_POLICY_DENIAL"] = 1

    if (control == "TOOL_AUTHZ" && outcome == "DENIED")
        actual["TOOL_AUTHORIZATION_DENIAL"] = 1

    if (control == "MCP_POLICY" && outcome == "DENIED")
        actual["MCP_POLICY_DENIAL"] = 1

    if (control == "DATA_POLICY" && outcome == "DENIED")
        actual["SENSITIVE_EXPORT_DENIAL"] = 1

    if (control == "RESOURCE_LIMIT" && outcome == "DENIED")
        resource_fail[actor]++

    if (control == "WORKLOAD_POLICY" && outcome == "DENIED")
        actual["WORKLOAD_PRIVILEGE_DENIAL"] = 1

    if (control == "AUTH_SUCCESS" ||
        control == "AUTHZ_ALLOW" ||
        control == "RAG_AUTHZ_ALLOW" ||
        control == "TOOL_ALLOW") {

        allowed_count++

        if (outcome != "ALLOWED")
            allowed_negative_fail++
    }
}

END {
    for (actor in auth_fail)
        if (auth_fail[actor] >= 3)
            actual["REPEATED_AUTH_FAILURE"] = 1

    for (actor in resource_fail)
        if (resource_fail[actor] >= 3)
            actual["REPEATED_RESOURCE_VIOLATION"] = 1

    expected_count = 0
    actual_count = 0
    missing_count = 0
    unexpected_count = 0

    for (name in expected) {
        expected_count++

        if (name in actual)
            actual_count++
        else {
            print "MISSING=" name
            missing_count++
        }
    }

    for (name in actual)
        if (!(name in expected)) {
            print "UNEXPECTED=" name
            unexpected_count++
        }

    # Stable output order.
    order[1] = "AGENT_POLICY_DENIAL"
    order[2] = "CROSS_TENANT_ACCESS"
    order[3] = "CROSS_USER_ACCESS"
    order[4] = "MCP_POLICY_DENIAL"
    order[5] = "REPEATED_AUTH_FAILURE"
    order[6] = "REPEATED_RESOURCE_VIOLATION"
    order[7] = "SENSITIVE_EXPORT_DENIAL"
    order[8] = "TOOL_AUTHORIZATION_DENIAL"
    order[9] = "UNAUTHORIZED_MEMORY_ACCESS"
    order[10] = "UNAUTHORIZED_RAG_RETRIEVAL"
    order[11] = "WORKLOAD_IDENTITY_FAILURE"
    order[12] = "WORKLOAD_PRIVILEGE_DENIAL"

    for (i = 1; i <= 12; i++)
        if (order[i] in actual)
            print "DETECTION=" order[i]

    print "SYNTHETIC_EVENT_COUNT=" event_count
    print "EXPECTED_DETECTIONS=" expected_count
    print "ACTUAL_DETECTIONS=" actual_count
    print "ALLOWED_EVENT_COUNT=" allowed_count

    if (allowed_negative_fail == 0)
        print "ALLOWED_EVENT_NEGATIVE_CONTROL=PASS"
    else
        print "ALLOWED_EVENT_NEGATIVE_CONTROL=FAIL"

    if (event_count == 20 &&
        expected_count == 12 &&
        actual_count == 12 &&
        missing_count == 0 &&
        unexpected_count == 0 &&
        allowed_negative_fail == 0) {

        print "PHASE20_DETECTION_GATE=PASS"
        exit 0
    }

    print "PHASE20_DETECTION_GATE=FAIL"
    exit 1
}
