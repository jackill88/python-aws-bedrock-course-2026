import pytest

from shared.testing import load_challenge

tool_idempotency_key = load_challenge(
    "06_agents_and_orchestration", "tool_idempotency_key.py"
).tool_idempotency_key


def test_reads() -> None:
    assert tool_idempotency_key("read") == "none_required"


def test_mutations() -> None:
    assert tool_idempotency_key("write") == "required"
    assert tool_idempotency_key("irreversible") == "required"


def test_unknown() -> None:
    with pytest.raises(ValueError):
        tool_idempotency_key("think")
