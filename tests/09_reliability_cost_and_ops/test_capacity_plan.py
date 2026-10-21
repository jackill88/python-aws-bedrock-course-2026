import pytest

from shared.testing import load_challenge

capacity_plan = load_challenge(
    "09_reliability_cost_and_ops", "capacity_plan.py"
).capacity_plan


def test_batch() -> None:
    assert capacity_plan(False, 10, 10, True) == "batch"


def test_provisioned_shapes() -> None:
    assert capacity_plan(True, 2, 3, False) == "provisioned"
    assert capacity_plan(True, 2, 3.1, False) == "provisioned_with_burst_buffer"


def test_on_demand() -> None:
    assert capacity_plan(True, 1.9, 4, False) == "on_demand"
    assert capacity_plan(False, 10, 12, False) == "on_demand"


def test_interactive_backfill_is_not_batch() -> None:
    assert capacity_plan(True, 0.2, 0.2, True) == "on_demand"


def test_invalid_rates() -> None:
    with pytest.raises(ValueError):
        capacity_plan(True, 5, 4, False)
    with pytest.raises(ValueError):
        capacity_plan(False, -1, 0, True)
