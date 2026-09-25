import json
import os
import pathlib
import unittest


ROOT = pathlib.Path(
    os.environ.get(
        "PHASE14_REPO_ROOT",
        "/workspace",
    )
)

DATASET = (
    ROOT
    / "docs/security/fixtures/"
      "phase14-synthetic-red-team-dataset-v1.jsonl"
)

ORACLES = (
    ROOT
    / "docs/security/fixtures/"
      "phase14-security-oracles-v1.json"
)


class TestPhase14EvaluatorIntegrity(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = [
            json.loads(line)
            for line in DATASET.read_text().splitlines()
            if line.strip()
        ]

        cls.oracles = json.loads(
            ORACLES.read_text()
        )

    def test_dataset_is_versioned_synthetic_and_unique(
        self,
    ) -> None:
        self.assertEqual(
            len(self.cases),
            24,
        )

        self.assertEqual(
            len({case["id"] for case in self.cases}),
            24,
        )

        self.assertTrue(
            all(
                case["synthetic"] is True
                for case in self.cases
            )
        )

    def test_unexecuted_cases_are_not_auto_promoted(
        self,
    ) -> None:
        self.assertTrue(
            all(
                case["status"] == "NOT_VERIFIED"
                for case in self.cases
            )
        )

    def test_required_attack_domains_are_present(
        self,
    ) -> None:
        categories = {
            case["category"]
            for case in self.cases
        }

        required = {
            "direct_prompt_injection",
            "indirect_prompt_injection",
            "retrieval_poisoning",
            "cross_tenant_retrieval",
            "sensitive_data_exposure",
            "unauthorized_action",
            "mcp_scope_abuse",
            "tool_shadowing",
            "structured_output",
            "memory_injection",
            "multi_turn_attack",
            "multi_agent_delegation",
            "recursive_tool_loop",
            "security_control_regression",
        }

        self.assertTrue(
            required <= categories
        )

    def test_model_dependent_claims_require_repeated_trials(
        self,
    ) -> None:
        policy = self.oracles["policy"]

        self.assertEqual(
            policy["model_dependent_claims"],
            "REQUIRE_REPEATED_TRIALS",
        )

    def test_thresholds_are_not_invented_before_baseline(
        self,
    ) -> None:
        policy = self.oracles["policy"]

        self.assertEqual(
            policy["thresholds"],
            "ESTABLISH_AFTER_MEASURED_BASELINE",
        )

    def test_exception_process_is_complete(
        self,
    ) -> None:
        required = {
            "owner",
            "reason",
            "expiry",
            "compensating_control",
            "rollback",
        }

        self.assertEqual(
            set(
                self.oracles["policy"][
                    "exceptions_require"
                ]
            ),
            required,
        )


if __name__ == "__main__":
    unittest.main()
