"""
Challenge: SLO Status
Module 09: Reliability, Cost, and Operations

Implement the function(s) below. Run tests with:
    pytest tests/09_reliability_cost_and_ops/ -v
"""

def slo_status(
    availability: float,
    groundedness: float,
    p95_ms: float,
    targets: dict,
) -> str:
    """
    targets must contain availability, groundedness, and p95_ms.
    Missing key -> ValueError.

    Record a breach when:
    - availability < targets["availability"]  -> "availability"
    - groundedness < targets["groundedness"] -> "quality"
    - p95_ms > targets["p95_ms"]             -> "latency"

    No breaches -> "met"
    One breach -> that name plus "_breach"
    More than one -> "multi_breach"
    """
    pass
