import pytest

from shared.testing import load_challenge

fallback_route = load_challenge(
    "02_model_strategy", "fallback_route.py"
).fallback_route


@pytest.mark.parametrize(
    "error_code",
    ["ThrottlingException", "ServiceQuotaExceededException"],
)
def test_backoff_same_model(error_code: str) -> None:
    assert fallback_route(error_code) == "same_model_backoff"


@pytest.mark.parametrize(
    "error_code",
    ["ModelTimeoutException", "ModelErrorException", "InternalServerException"],
)
def test_fallback_model(error_code: str) -> None:
    assert fallback_route(error_code) == "fallback_model"


@pytest.mark.parametrize(
    "error_code",
    ["ValidationException", "AccessDeniedException"],
)
def test_fail_closed(error_code: str) -> None:
    assert fallback_route(error_code) == "fail_closed"


def test_unknown_error() -> None:
    with pytest.raises(ValueError):
        fallback_route("ExpiredTokenException")
