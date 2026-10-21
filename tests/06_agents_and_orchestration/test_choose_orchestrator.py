import pytest

from shared.testing import load_challenge

choose_orchestrator = load_challenge(
    "06_agents_and_orchestration", "choose_orchestrator.py"
).choose_orchestrator


def test_irreversible_wins() -> None:
    assert (
        choose_orchestrator("flexible", "irreversible", True)
        == "workflow_with_human_approval"
    )
    assert (
        choose_orchestrator("strict", "irreversible", False)
        == "workflow_with_human_approval"
    )


def test_strict_read_is_workflow() -> None:
    assert choose_orchestrator("strict", "read", True) == "workflow"


def test_open_read_and_write() -> None:
    assert choose_orchestrator("flexible", "read", True) == "agent"
    assert choose_orchestrator("flexible", "write", True) == "hybrid"


def test_closed_flexible_is_workflow() -> None:
    assert choose_orchestrator("flexible", "read", False) == "workflow"
    assert choose_orchestrator("flexible", "write", False) == "workflow"


def test_unknown() -> None:
    with pytest.raises(ValueError):
        choose_orchestrator("loose", "read", True)
    with pytest.raises(ValueError):
        choose_orchestrator("flexible", "delete", True)
