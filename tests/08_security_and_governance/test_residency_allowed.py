from shared.testing import load_challenge

residency_allowed = load_challenge(
    "08_security_and_governance", "residency_allowed.py"
).residency_allowed


def test_all_destinations_must_be_listed() -> None:
    assert residency_allowed(["eu-west-1"], ["eu-west-1", "eu-central-1"]) is True
    assert residency_allowed(
        ["eu-west-1", "us-east-1"], ["eu-west-1", "eu-central-1"]
    ) is False


def test_empty_processing_is_not_allowed() -> None:
    assert residency_allowed([], ["eu-west-1"]) is False


def test_duplicates_are_fine() -> None:
    assert residency_allowed(["eu-west-1", "eu-west-1"], ["eu-west-1"]) is True
