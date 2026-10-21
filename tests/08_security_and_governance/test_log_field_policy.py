import pytest

from shared.testing import load_challenge

log_field_policy = load_challenge(
    "08_security_and_governance", "log_field_policy.py"
).log_field_policy


def test_keep() -> None:
    for field in ("request_id", "model_id", "latency_ms", "token_counts"):
        assert log_field_policy(field) == "keep"


def test_restricted_content() -> None:
    for field in ("prompt", "completion", "retrieved_text"):
        assert log_field_policy(field) == "redact_or_separate_restricted_store"


def test_drop_secrets() -> None:
    assert log_field_policy("api_key") == "drop"
    assert log_field_policy("authorization") == "drop"


def test_unknown() -> None:
    with pytest.raises(ValueError):
        log_field_policy("session_transcript")
