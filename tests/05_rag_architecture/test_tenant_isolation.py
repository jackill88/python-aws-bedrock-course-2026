import pytest

from shared.testing import load_challenge

tenant_isolation = load_challenge(
    "05_rag_architecture", "tenant_isolation.py"
).tenant_isolation


def test_classes() -> None:
    assert tenant_isolation("regulated_plus", 3) == "account_per_tenant"
    assert tenant_isolation("strict", 400) == "index_per_tenant"
    assert tenant_isolation("standard", 50) == "shared_index_metadata_filter"


def test_count_does_not_weaken_regulation() -> None:
    assert tenant_isolation("regulated_plus", 5000) == "account_per_tenant"


def test_invalid() -> None:
    with pytest.raises(ValueError):
        tenant_isolation("standard", 0)
    with pytest.raises(ValueError):
        tenant_isolation("casual", 2)
