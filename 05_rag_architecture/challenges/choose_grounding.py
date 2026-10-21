"""
Challenge: Choose Grounding
Module 05: RAG Architecture

Implement the function(s) below. Run tests with:
    pytest tests/05_rag_architecture/ -v
"""


def choose_grounding(
    change_rate: str,
    corpus_tokens: int,
    context_budget: int,
    labeled_examples: int,
    need_behavior_change: bool,
) -> str:
    """
    Return "prompt_only", "long_context", "rag", "finetune", or "rag_plus_finetune".

    change_rate: "rare", "weekly", or "daily_or_faster". Else ValueError.
    Negative corpus_tokens, context_budget, or labeled_examples -> ValueError.

    volatile = change_rate in {"weekly", "daily_or_faster"}
    fits = corpus_tokens <= context_budget
    behavior = need_behavior_change and labeled_examples >= 500

    1. volatile and behavior -> "rag_plus_finetune"
    2. volatile or not fits:
         if not volatile and corpus_tokens <= 200_000 -> "long_context"
         else -> "rag"
    3. behavior -> "finetune"
    4. else -> "prompt_only"
    """
    pass
