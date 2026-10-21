import pytest

from shared.testing import load_challenge

guardrail_stages = load_challenge(
    "07_guardrails_and_safety", "guardrail_stages.py"
).guardrail_stages


def test_surfaces() -> None:
    assert guardrail_stages("user_chat") == ["input", "output"]
    assert guardrail_stages("tool_arguments") == ["input"]
    assert guardrail_stages("final_answer_with_sources") == ["output", "grounding"]
    assert guardrail_stages("batch_generation") == ["output"]


def test_returns_a_copy() -> None:
    first = guardrail_stages("user_chat")
    first.append("extra")
    assert guardrail_stages("user_chat") == ["input", "output"]


def test_unknown() -> None:
    with pytest.raises(ValueError):
        guardrail_stages("dns")
