"""
Challenge: Cache Decision
Module 03: Inference Architecture

Implement the function(s) below. Run tests with:
    pytest tests/03_inference_architecture/ -v
"""


def cache_decision(
    prefix_tokens: int,
    identical_prefix_reuse_per_hour: int,
    prefix_stable: bool,
) -> str:
    """
    Return "cache" or "skip".

    Raise ValueError if either count is negative.

    "skip" unless all of these hold:
    - prefix_stable
    - prefix_tokens >= 1024
    - identical_prefix_reuse_per_hour >= 5
    """
    pass
