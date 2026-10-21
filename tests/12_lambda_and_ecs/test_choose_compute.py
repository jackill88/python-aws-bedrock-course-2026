import pytest

from shared.testing import load_challenge

choose_compute = load_challenge(
    "12_lambda_and_ecs", "choose_compute.py"
).choose_compute


def test_short_event_and_stream_stay_on_lambda() -> None:
    assert choose_compute("event", 30) == "lambda"
    assert choose_compute("response_stream", 900) == "lambda"
    assert choose_compute("event", 0) == "lambda"


def test_held_session_is_fargate() -> None:
    assert choose_compute("held_session", 5) == "ecs_fargate"


def test_over_lambda_max_is_fargate() -> None:
    assert choose_compute("event", 901) == "ecs_fargate"
    assert choose_compute("response_stream", 901) == "ecs_fargate"


def test_invalid() -> None:
    with pytest.raises(ValueError):
        choose_compute("gpu", 10)
    with pytest.raises(ValueError):
        choose_compute("event", -1)
