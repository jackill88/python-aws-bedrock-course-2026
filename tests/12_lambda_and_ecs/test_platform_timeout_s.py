import pytest

from shared.testing import load_challenge

platform_timeout_s = load_challenge(
    "12_lambda_and_ecs", "platform_timeout_s.py"
).platform_timeout_s


def test_ceilings() -> None:
    assert platform_timeout_s("api_gateway") == 29
    assert platform_timeout_s("lambda_function_url") == 900
    assert platform_timeout_s("alb") == 4000
    assert platform_timeout_s("ecs_task") is None


def test_unknown_edge() -> None:
    with pytest.raises(ValueError):
        platform_timeout_s("cloudfront")
