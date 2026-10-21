import pytest

from shared.testing import load_challenge

fit_token_budget = load_challenge(
    "03_inference_architecture", "fit_token_budget.py"
).fit_token_budget


def test_already_fits() -> None:
    assert fit_token_budget(1000, 100, 200, 300, 200) == {
        "fits": True,
        "drop_retrieval": 0,
        "drop_history": 0,
    }


def test_drop_retrieval_before_history() -> None:
    assert fit_token_budget(1000, 100, 400, 500, 200) == {
        "fits": False,
        "drop_retrieval": 200,
        "drop_history": 0,
    }


def test_then_drop_history() -> None:
    assert fit_token_budget(500, 100, 400, 200, 100) == {
        "fits": False,
        "drop_retrieval": 200,
        "drop_history": 100,
    }


def test_system_and_reserve_must_fit() -> None:
    with pytest.raises(ValueError):
        fit_token_budget(150, 100, 10, 10, 80)


def test_negative() -> None:
    with pytest.raises(ValueError):
        fit_token_budget(100, -1, 0, 0, 10)
