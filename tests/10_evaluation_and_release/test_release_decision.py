import pytest

from shared.testing import load_challenge

release_decision = load_challenge(
    "10_evaluation_and_release", "release_decision.py"
).release_decision


def test_ship() -> None:
    assert release_decision(0.8, True, 10, 0.0) == "ship"
    assert release_decision(0.9, True, 40, 0.05) == "ship"


def test_blocks() -> None:
    assert release_decision(0.99, False, 0, 0.1) == "block"
    assert release_decision(0.79, True, 0, 0.1) == "block"
    assert release_decision(0.9, True, 0, -0.02) == "block"
    assert release_decision(0.9, True, 25.1, 0.049) == "block"


def test_cost_boundary() -> None:
    assert release_decision(0.9, True, 25, 0.0) == "ship"


def test_bad_offline() -> None:
    with pytest.raises(ValueError):
        release_decision(1.2, True, 0, 0)
