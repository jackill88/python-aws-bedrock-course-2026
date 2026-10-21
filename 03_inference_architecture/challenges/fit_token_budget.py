"""
Challenge: Fit Token Budget
Module 03: Inference Architecture

Implement the function(s) below. Run tests with:
    pytest tests/03_inference_architecture/ -v
"""


def fit_token_budget(
    limit: int,
    system_tokens: int,
    history_tokens: int,
    retrieval_tokens: int,
    output_reserve: int,
) -> dict:
    """
    Return {"fits": bool, "drop_retrieval": int, "drop_history": int}.

    Raise ValueError if any argument is negative, or if
    system_tokens + output_reserve > limit.

    overflow = max(0, system + history + retrieval + output_reserve - limit)
    Drop retrieval first, then history.
    fits is True only when overflow == 0.
    """
    pass
