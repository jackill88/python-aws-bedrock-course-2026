"""
Challenge: Choose Consumption Mode
Module 01: Bedrock Platform

Implement the function(s) below. Run tests with:
    pytest tests/01_bedrock_platform/ -v
"""


def choose_consumption_mode(
    requests_per_day: int,
    latency_sensitive: bool,
    predictable_baseline: bool,
    async_ok: bool,
) -> str:
    """
    Return "batch", "provisioned", or "on_demand".

    Order:
    1. "batch" when async_ok and not latency_sensitive.
    2. "provisioned" when latency_sensitive, predictable_baseline,
       and requests_per_day >= 100_000.
    3. Otherwise "on_demand".

    Raise ValueError if requests_per_day < 0.
    """
    pass
