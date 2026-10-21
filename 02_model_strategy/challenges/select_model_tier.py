"""
Challenge: Select Model Tier
Module 02: Model Strategy

Implement the function(s) below. Run tests with:
    pytest tests/02_model_strategy/ -v
"""


def select_model_tier(task: str, latency_class: str, needs_tools: bool) -> str:
    """
    Return "small", "balanced", or "frontier".

    latency_class must be "interactive" or "batch" (else ValueError).
    It does not change the tier by itself.

    task map:
        complex_reasoning -> frontier
        agent -> balanced
        rag_answer -> balanced
        classify -> small
        extract -> small
    Unknown task -> ValueError.

    If needs_tools and the mapped tier is "small", upgrade to "balanced".
    """
    pass
