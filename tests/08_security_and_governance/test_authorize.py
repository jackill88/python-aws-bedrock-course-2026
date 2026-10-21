import pytest

from shared.testing import load_challenge

authorize = load_challenge(
    "08_security_and_governance", "authorize.py"
).authorize


def test_admin_allows_all() -> None:
    for action in (
        "invoke_prod",
        "invoke_dev",
        "create_guardrail",
        "read_invocation_logs",
        "manage_provisioned_throughput",
        "retrieve_kb",
    ):
        assert authorize("platform_admin", action) == "allow"


def test_runtime_is_narrow() -> None:
    assert authorize("app_runtime", "invoke_prod") == "allow"
    assert authorize("app_runtime", "retrieve_kb") == "allow"
    assert authorize("app_runtime", "read_invocation_logs") == "deny"
    assert authorize("app_runtime", "invoke_dev") == "deny"


def test_other_roles() -> None:
    assert authorize("data_scientist", "invoke_dev") == "allow"
    assert authorize("data_scientist", "invoke_prod") == "deny"
    assert authorize("auditor", "read_invocation_logs") == "allow"
    assert authorize("auditor", "invoke_dev") == "deny"
    assert authorize("product_dev", "invoke_dev") == "allow"
    assert authorize("product_dev", "retrieve_kb") == "deny"


def test_unknown() -> None:
    with pytest.raises(ValueError):
        authorize("intern", "invoke_dev")
    with pytest.raises(ValueError):
        authorize("auditor", "delete_account")
