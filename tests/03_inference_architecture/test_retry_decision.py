import pytest

from shared.testing import load_challenge

retry_decision = load_challenge(
    "03_inference_architecture", "retry_decision.py"
).retry_decision


def test_throttle_retries_until_cap() -> None:
    assert retry_decision("ThrottlingException", 1, 3, False) == "retry"
    assert retry_decision("ThrottlingException", 3, 3, True) == "fail"


def test_timeout_respects_idempotency() -> None:
    assert retry_decision("ModelTimeoutException", 1, 3, True) == "retry"
    assert retry_decision("InternalServerException", 1, 3, False) == "fail"
    assert retry_decision("ServiceUnavailableException", 2, 4, True) == "retry"


def test_validation_and_access_fail_closed() -> None:
    assert retry_decision("ValidationException", 1, 5, True) == "fail"
    assert retry_decision("AccessDeniedException", 1, 5, True) == "fail"


def test_bad_counts_and_unknown_error() -> None:
    with pytest.raises(ValueError):
        retry_decision("ThrottlingException", 0, 3, True)
    with pytest.raises(ValueError):
        retry_decision("ThrottlingException", 1, 0, True)
    with pytest.raises(ValueError):
        retry_decision("ServiceQuotaExceededException", 1, 3, True)
