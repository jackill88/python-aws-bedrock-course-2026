import pytest

from shared.testing import load_challenge

slo_status = load_challenge(
    "09_reliability_cost_and_ops", "slo_status.py"
).slo_status

TARGETS = {"availability": 0.995, "groundedness": 0.9, "p95_ms": 3000}


def test_met() -> None:
    assert slo_status(0.999, 0.95, 2800, TARGETS) == "met"
    assert slo_status(0.995, 0.9, 3000, TARGETS) == "met"


def test_single_breaches() -> None:
    assert slo_status(0.99, 0.95, 1000, TARGETS) == "availability_breach"
    assert slo_status(0.999, 0.5, 1000, TARGETS) == "quality_breach"
    assert slo_status(0.999, 0.95, 3001, TARGETS) == "latency_breach"


def test_multi() -> None:
    assert slo_status(0.5, 0.5, 9000, TARGETS) == "multi_breach"


def test_missing_target() -> None:
    with pytest.raises(ValueError):
        slo_status(1, 1, 1, {"availability": 0.9})
