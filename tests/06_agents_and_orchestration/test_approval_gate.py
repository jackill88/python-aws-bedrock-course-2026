import pytest

from shared.testing import load_challenge

approval_gate = load_challenge(
    "06_agents_and_orchestration", "approval_gate.py"
).approval_gate


def test_reads_do_not_page() -> None:
    assert approval_gate("read", True, 50_000) is False


def test_irreversible_always() -> None:
    assert approval_gate("irreversible", False, 0) is True


def test_prod_write_threshold() -> None:
    assert approval_gate("write", True, 1000) is True
    assert approval_gate("write", True, 999) is False


def test_large_write_outside_prod() -> None:
    assert approval_gate("write", False, 10_000) is True
    assert approval_gate("write", False, 9_999) is False


def test_invalid() -> None:
    with pytest.raises(ValueError):
        approval_gate("admin", True, 10)
    with pytest.raises(ValueError):
        approval_gate("write", True, -1)
