import pytest

from shared.testing import load_challenge

network_path = load_challenge(
    "08_security_and_governance", "network_path.py"
).network_path


def test_paths() -> None:
    assert network_path("public") == "public_endpoint_ok"
    assert network_path("confidential") == "interface_vpc_endpoint"
    assert network_path("restricted") == "interface_vpc_endpoint"


def test_unknown() -> None:
    with pytest.raises(ValueError):
        network_path("internal")
