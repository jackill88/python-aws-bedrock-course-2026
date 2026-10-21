import pytest

from shared.testing import load_challenge

judge_trust = load_challenge(
    "10_evaluation_and_release", "judge_trust.py"
).judge_trust


def test_methods() -> None:
    assert judge_trust("format_compliance") == "automatic_ok"
    assert judge_trust("groundedness_against_sources") == "model_judge_plus_audit_sample"
    assert judge_trust("helpfulness") == "human_sample"
    assert judge_trust("policy_violation") == "automatic_plus_human_on_positive"


def test_unknown() -> None:
    with pytest.raises(ValueError):
        judge_trust("vibes")
