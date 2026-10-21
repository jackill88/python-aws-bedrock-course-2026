"""
Challenge: Grounding Verdict
Module 07: Guardrails and Safety

Implement the function(s) below. Run tests with:
    pytest tests/07_guardrails_and_safety/ -v
"""

def grounding_verdict(supported_claims: int, total_claims: int, min_ratio: float) -> str:
    """
    Return "pass" or "fail".

    Raise ValueError if counts are negative, supported_claims > total_claims,
    or min_ratio is outside [0, 1].

    total_claims == 0 -> "pass".
    Otherwise "pass" when supported_claims / total_claims >= min_ratio, else "fail".
    """
    pass
