"""
Challenge: Release Decision
Module 10: Evaluation and Release

Implement the function(s) below. Run tests with:
    pytest tests/10_evaluation_and_release/ -v
"""

def release_decision(
    offline: float,
    safety_passed: bool,
    cost_increase_pct: float,
    shadow_quality_delta: float,
) -> str:
    """
    Return "ship" or "block".

    Raise ValueError if offline is outside [0, 1].

    Block when safety_passed is false, offline < 0.8,
    shadow_quality_delta <= -0.02, or
    (cost_increase_pct > 25 and shadow_quality_delta < 0.05).
    Otherwise ship.
    """
    pass
