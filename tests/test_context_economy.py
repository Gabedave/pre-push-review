import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = (
    "approval-and-snapshot.md",
    "high-risk-review.md",
    "independent-review.md",
    "external-research.md",
    "reconciliation.md",
    "final-verification.md",
)


class ContextEconomy(unittest.TestCase):
    def test_entrypoint_stays_within_context_budget(self):
        self.assertLessEqual(len((ROOT / "SKILL.md").read_text()), 14_000)

    def test_conditional_guidance_is_routed_through_references(self):
        entrypoint = (ROOT / "SKILL.md").read_text()
        for name in REFERENCES:
            with self.subTest(reference=name):
                self.assertIn(f"references/{name}", entrypoint)
                self.assertTrue((ROOT / "references" / name).is_file())

        self.assertIn("Always read [approval and snapshot]", entrypoint)
        self.assertIn("always read [final verification]", entrypoint)
        self.assertIn("For high-risk work", entrypoint)
        self.assertIn("Only when a material conclusion depends", entrypoint)
        self.assertIn("If a blocker or material disagreement exists", entrypoint)

    def test_universal_focused_verification_stays_always_reachable(self):
        approval = (ROOT / "references" / "approval-and-snapshot.md").read_text()
        high_risk = (ROOT / "references" / "high-risk-review.md").read_text()
        for obligation in (
            "focused regression tests for changed behavior and important failure paths",
            "the smallest relevant type, syntax, formatting, or static check",
            "deterministic integration evidence when risk cannot be proven at unit level",
            "Defer slow broad suites",
        ):
            with self.subTest(obligation=obligation):
                self.assertIn(obligation, approval)
                self.assertNotIn(obligation, high_risk)

    def test_independent_reviewer_owns_criterion_mapping(self):
        review = (ROOT / "references" / "independent-review.md").read_text()
        self.assertIn(
            "verify or produce every criterion's evidence-and-result mapping", review
        )

    def test_split_preserves_review_contract(self):
        content = [(ROOT / "SKILL.md").read_text()]
        content.extend(
            (ROOT / "references" / name).read_text() for name in REFERENCES
        )
        combined = "\n".join(content)
        for contract in (
            "criterion -> changed seam -> focused evidence -> broad evidence -> result",
            "APPROVAL CONTRACT: VERIFIED",
            "APPROVAL CONTRACT: NOT VERIFIED",
            "APPROVAL CONTRACT: HUMAN DECISION REQUIRED",
            "INDEPENDENT REVIEW: PERFORMED",
            "INDEPENDENT REVIEW: NOT PERFORMED",
            "CONSENSUS: ACHIEVED",
            "CONSENSUS: NOT ACHIEVED",
            "CONSENSUS: HUMAN DECISION REQUIRED",
            "STATUS: READY FOR TEAM REVIEW",
            "STATUS: NOT READY FOR TEAM REVIEW",
            "STATUS: REVIEW INCOMPLETE",
        ):
            with self.subTest(contract=contract):
                self.assertIn(contract, combined)


if __name__ == "__main__":
    unittest.main()
