"""
Challenge: Token Cost
Module 09: Reliability, Cost, and Operations

Implement the function(s) below. Run tests with:
    pytest tests/09_reliability_cost_and_ops/ -v
"""

def token_cost_usd(
    input_tokens: int,
    output_tokens: int,
    cache_read_tokens: int,
    cache_write_tokens: int,
    prices: dict,
) -> float:
    """
    USD cost. prices are USD per million tokens with keys
    input, output, cache_read, cache_write.

    Missing price key or any negative token count -> ValueError.
    Do not add cache tokens into input_tokens; the caller already split them.
    """
    pass
