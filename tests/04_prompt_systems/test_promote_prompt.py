import pytest

from shared.testing import load_challenge

promote_prompt = load_challenge(
    "04_prompt_systems", "promote_prompt.py"
).promote_prompt


def test_all_gates_promote() -> None:
    assert promote_prompt(0.85, False, True, True) == "promote"
    assert promote_prompt(1.0, False, True, True) == "promote"


def test_each_failed_gate_holds() -> None:
    assert promote_prompt(0.849, False, True, True) == "hold"
    assert promote_prompt(0.99, True, True, True) == "hold"
    assert promote_prompt(0.99, False, False, True) == "hold"
    assert promote_prompt(0.99, False, True, False) == "hold"


def test_score_out_of_range() -> None:
    with pytest.raises(ValueError):
        promote_prompt(1.01, False, True, True)
    with pytest.raises(ValueError):
        promote_prompt(-0.01, False, True, True)
