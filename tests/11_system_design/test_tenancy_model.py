import pytest

from shared.testing import load_challenge

tenancy_model = load_challenge(
    "11_system_design", "tenancy_model.py"
).tenancy_model


def test_classes() -> None:
    assert tenancy_model("regulatory", 2) == "account_per_tenant"
    assert tenancy_model("strong", 20) == "index_per_tenant"
    assert tenancy_model("logical", 100) == "shared_index_metadata_filter"


def test_count_does_not_downgrade() -> None:
    assert tenancy_model("regulatory", 10_000) == "account_per_tenant"


def test_invalid() -> None:
    with pytest.raises(ValueError):
        tenancy_model("logical", 0)
    with pytest.raises(ValueError):
        tenancy_model("public", 3)
