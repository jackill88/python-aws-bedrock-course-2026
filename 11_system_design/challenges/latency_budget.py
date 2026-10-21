"""
Challenge: Latency Budget
Module 11: System Design

Implement the function(s) below. Run tests with:
    pytest tests/11_system_design/ -v
"""

def latency_budget(total_ms: int) -> dict:
    """
    Split total_ms into integer milliseconds.

    Raise ValueError if total_ms < 100.

    Percentages:
        retrieval 15, rerank 10, model_ttft 35,
        generation_buffer 25, guardrails 15

    Use integer division. Add the remainder so the values sum to total_ms
    onto model_ttft.

    Return a dict with those five keys.
    """
    pass
