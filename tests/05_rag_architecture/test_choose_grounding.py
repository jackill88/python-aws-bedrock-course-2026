import pytest

from shared.testing import load_challenge

choose_grounding = load_challenge(
    "05_rag_architecture", "choose_grounding.py"
).choose_grounding


def test_volatile_knowledge_is_rag() -> None:
    assert choose_grounding("daily_or_faster", 10_000, 8_000, 0, False) == "rag"
    assert choose_grounding("weekly", 1_000, 8_000, 10, False) == "rag"


def test_volatile_plus_behavior() -> None:
    assert (
        choose_grounding("daily_or_faster", 10_000, 8_000, 2_000, True)
        == "rag_plus_finetune"
    )


def test_long_context_window() -> None:
    assert choose_grounding("rare", 120_000, 8_000, 0, False) == "long_context"


def test_too_large_for_long_context() -> None:
    assert choose_grounding("rare", 500_000, 8_000, 0, False) == "rag"


def test_finetune_and_prompt_only() -> None:
    assert choose_grounding("rare", 2_000, 8_000, 800, True) == "finetune"
    assert choose_grounding("rare", 2_000, 8_000, 800, False) == "prompt_only"
    assert choose_grounding("rare", 2_000, 8_000, 100, True) == "prompt_only"


def test_invalid() -> None:
    with pytest.raises(ValueError):
        choose_grounding("hourly", 10, 10, 0, False)
    with pytest.raises(ValueError):
        choose_grounding("rare", -1, 10, 0, False)
