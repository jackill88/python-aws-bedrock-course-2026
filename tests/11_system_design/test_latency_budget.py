import pytest

from shared.testing import load_challenge

latency_budget = load_challenge(
    "11_system_design", "latency_budget.py"
).latency_budget


def test_two_seconds() -> None:
    assert latency_budget(2000) == {
        "retrieval": 300,
        "rerank": 200,
        "model_ttft": 700,
        "generation_buffer": 500,
        "guardrails": 300,
    }


def test_remainder_goes_to_ttft() -> None:
    alloc = latency_budget(101)
    assert sum(alloc.values()) == 101
    assert alloc["retrieval"] == 15
    assert alloc["rerank"] == 10
    assert alloc["generation_buffer"] == 25
    assert alloc["guardrails"] == 15
    assert alloc["model_ttft"] == 36


def test_too_small() -> None:
    with pytest.raises(ValueError):
        latency_budget(99)
