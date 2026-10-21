import pytest

from shared.testing import load_challenge

select_model_tier = load_challenge(
    "02_model_strategy", "select_model_tier.py"
).select_model_tier


def test_reasoning_is_frontier() -> None:
    assert select_model_tier("complex_reasoning", "interactive", False) == "frontier"
    assert select_model_tier("complex_reasoning", "batch", True) == "frontier"


def test_rag_and_agent_are_balanced() -> None:
    assert select_model_tier("rag_answer", "interactive", False) == "balanced"
    assert select_model_tier("agent", "batch", False) == "balanced"


def test_classify_and_extract_are_small_without_tools() -> None:
    assert select_model_tier("classify", "interactive", False) == "small"
    assert select_model_tier("extract", "batch", False) == "small"


def test_tools_upgrade_small_only() -> None:
    assert select_model_tier("extract", "interactive", True) == "balanced"
    assert select_model_tier("rag_answer", "interactive", True) == "balanced"


@pytest.mark.parametrize(
    ("task", "latency_class"),
    [("summarize", "interactive"), ("classify", "realtime")],
)
def test_unknown_inputs(task: str, latency_class: str) -> None:
    with pytest.raises(ValueError):
        select_model_tier(task, latency_class, False)
