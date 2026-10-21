"""
Challenge: Promote Prompt
Module 04: Prompt Systems

Implement the function(s) below. Run tests with:
    pytest tests/04_prompt_systems/ -v
"""


def promote_prompt(
    offline_score: float,
    regression: bool,
    injection_suite_passed: bool,
    human_review: bool,
) -> str:
    """
    Return "promote" or "hold".

    Raise ValueError if offline_score is outside [0.0, 1.0].

    "promote" only when offline_score >= 0.85, regression is false,
    injection_suite_passed is true, and human_review is true.
    Otherwise "hold".
    """
    pass
