"""
Challenge: Capacity Plan
Module 09: Reliability, Cost, and Operations

Implement the function(s) below. Run tests with:
    pytest tests/09_reliability_cost_and_ops/ -v
"""

def capacity_plan(
    p95_latency_sensitive: bool,
    steady_rps: float,
    peak_rps: float,
    async_backfill: bool,
) -> str:
    """
    Return "batch", "provisioned", "provisioned_with_burst_buffer", or "on_demand".

    Raise ValueError if a rate is negative or peak_rps < steady_rps.

    1. async_backfill and not p95_latency_sensitive -> batch
    2. p95_latency_sensitive and steady_rps >= 2:
         peak_rps <= steady_rps * 1.5 -> provisioned
         else -> provisioned_with_burst_buffer
    3. else -> on_demand
    """
    pass
