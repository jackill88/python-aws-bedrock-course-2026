import pytest

from shared.testing import load_challenge

pii_action = load_challenge(
    "07_guardrails_and_safety", "pii_action.py"
).pii_action


def test_logs_redact_all() -> None:
    for entity in ("email", "ssn", "name", "phone"):
        assert pii_action(entity, "logs") == "redact"


def test_ssn() -> None:
    assert pii_action("ssn", "external_user") == "block"
    assert pii_action("ssn", "internal_support") == "mask"


def test_name() -> None:
    assert pii_action("name", "internal_support") == "allow"
    assert pii_action("name", "external_user") == "mask"


def test_contact_channels() -> None:
    assert pii_action("email", "external_user") == "mask"
    assert pii_action("phone", "internal_support") == "mask"


def test_unknown() -> None:
    with pytest.raises(ValueError):
        pii_action("passport", "logs")
    with pytest.raises(ValueError):
        pii_action("email", "public_web")
