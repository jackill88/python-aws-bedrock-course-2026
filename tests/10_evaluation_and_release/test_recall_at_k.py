import pytest

from shared.testing import load_challenge

recall_at_k = load_challenge(
    "10_evaluation_and_release", "recall_at_k.py"
).recall_at_k


def test_basic_recall() -> None:
    assert recall_at_k(["a", "b", "c", "d"], {"b", "e"}, 3) == pytest.approx(0.5)


def test_duplicates_do_not_double_count() -> None:
    assert recall_at_k(["a", "b", "a"], {"a", "c"}, 3) == pytest.approx(0.5)


def test_cutoff() -> None:
    assert recall_at_k(["a", "b", "c"], {"c"}, 2) == pytest.approx(0.0)
    assert recall_at_k(["a", "b", "c"], {"c"}, 3) == pytest.approx(1.0)


def test_invalid() -> None:
    with pytest.raises(ValueError):
        recall_at_k(["a"], {"a"}, 0)
    with pytest.raises(ValueError):
        recall_at_k(["a"], set(), 1)
