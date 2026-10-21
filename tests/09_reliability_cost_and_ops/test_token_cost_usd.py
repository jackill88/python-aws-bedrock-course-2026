import pytest

from shared.testing import load_challenge

token_cost_usd = load_challenge(
    "09_reliability_cost_and_ops", "token_cost_usd.py"
).token_cost_usd

PRICES = {"input": 3.0, "output": 15.0, "cache_read": 0.3, "cache_write": 3.75}


def test_split_meters() -> None:
    cost = token_cost_usd(1_000_000, 1_000_000, 2_000_000, 0, PRICES)
    assert cost == pytest.approx(3 + 15 + 0.6)


def test_cache_write() -> None:
    cost = token_cost_usd(0, 0, 0, 1_000_000, PRICES)
    assert cost == pytest.approx(3.75)


def test_invalid() -> None:
    with pytest.raises(ValueError):
        token_cost_usd(1, 1, 1, 1, {"input": 1})
    with pytest.raises(ValueError):
        token_cost_usd(-1, 0, 0, 0, PRICES)
