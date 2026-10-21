import pytest

from shared.testing import load_challenge

async_duplicate_risk = load_challenge(
    "12_lambda_and_ecs", "async_duplicate_risk.py"
).async_duplicate_risk


def test_sync_is_client_retries_only() -> None:
    assert async_duplicate_risk("sync", "read") == "client_retries_only"
    assert async_duplicate_risk("sync", "write") == "client_retries_only"
    assert async_duplicate_risk("sync", "irreversible") == "client_retries_only"


def test_async_depends_on_side_effect() -> None:
    assert async_duplicate_risk("async", "read") == "duplicate_model_call"
    assert async_duplicate_risk("async", "write") == "duplicate_side_effect"
    assert async_duplicate_risk("async", "irreversible") == "duplicate_side_effect"


def test_unknown() -> None:
    with pytest.raises(ValueError):
        async_duplicate_risk("event", "read")
    with pytest.raises(ValueError):
        async_duplicate_risk("async", "delete")
