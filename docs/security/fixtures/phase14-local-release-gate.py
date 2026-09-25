import json
import pathlib
import sys

metrics = json.loads(
    pathlib.Path(
        sys.argv[1]
    ).read_text()
)

policy = json.loads(
    pathlib.Path(
        sys.argv[2]
    ).read_text()
)

d = metrics[
    "deterministic_metrics"
]

r = policy[
    "deterministic_release_requirements"
]

checks = {
    "suite_file_pass_rate":
        d[
            "suite_file_pass_rate"
        ]["value"]
        >= r[
            "suite_file_pass_rate_min"
        ],

    "deterministic_control_pass_rate":
        d[
            "deterministic_control_pass_rate"
        ]["value"]
        >= r[
            "deterministic_control_pass_rate_min"
        ],

    "repeated_evaluator_consistency":
        d[
            "repeated_evaluator_classification_consistency"
        ]["value"]
        >= r[
            "repeated_evaluator_consistency_min"
        ],

    "unknown_test_count_files":
        d[
            "unknown_test_count_files"
        ]["value"]
        <= r[
            "unknown_test_count_files_max"
        ],

    "external_model_provider_calls":
        metrics[
            "safety"
        ]["model_provider_calls"]
        <= r[
            "external_model_provider_calls_max"
        ],

    "network_mode":
        metrics[
            "safety"
        ]["runtime_network"]
        == r[
            "runtime_network_required"
        ],
}

for name, passed in checks.items():
    print(
        f"GATE_{name.upper()}="
        + (
            "PASS"
            if passed
            else "FAIL"
        )
    )

if not all(
    checks.values()
):
    print(
        "DETERMINISTIC_RELEASE_GATE=FAIL"
    )
    raise SystemExit(1)

print(
    "DETERMINISTIC_RELEASE_GATE=PASS"
)

print(
    "FULL_MODEL_ASSURANCE=NOT_GRANTED_NOT_MEASURED"
)

print(
    "RESULT=PASS_DETERMINISTIC_SCOPE_ONLY"
)
