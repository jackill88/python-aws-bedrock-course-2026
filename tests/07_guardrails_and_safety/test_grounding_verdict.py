import pytest

from shared.testing import load_challenge

grounding_verdict = load_challenge(
    "07_guardrails_and_safety", "grounding_verdict.py"
).grounding_verdict


def test_no_claims_passes() -> None:
    assert grounding_verdict(0, 0, 0.9) == "pass"


def test_ratio() -> None:
    assert grounding_verdict(9, 10, 0.9) == "pass"
    assert grounding_verdict(9, 10, 0.95) == "fail"
    assert grounding_verdict(10, 10, 1) == "pass"


def test_invalid() -> None:
    with pytest.raises(ValueError):
        grounding_verdict(3, 2, 0.5)
    with pytest.raises(ValueError):
        grounding_verdict(-1, 2, 0.5)
    with pytest.raises(ValueError):
        grounding_verdict(1, 1, 1.1)
