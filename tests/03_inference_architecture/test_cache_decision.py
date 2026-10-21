import pytest

from shared.testing import load_challenge

cache_decision = load_challenge(
    "03_inference_architecture", "cache_decision.py"
).cache_decision


def test_cache_when_all_gates_pass() -> None:
    assert cache_decision(1024, 5, True) == "cache"
    assert cache_decision(4096, 40, True) == "cache"


def test_skip_unstable_short_or_rare() -> None:
    assert cache_decision(4096, 100, False) == "skip"
    assert cache_decision(1023, 100, True) == "skip"
    assert cache_decision(1024, 4, True) == "skip"


def test_negative_counts() -> None:
    with pytest.raises(ValueError):
        cache_decision(-1, 10, True)
    with pytest.raises(ValueError):
        cache_decision(2048, -1, True)
