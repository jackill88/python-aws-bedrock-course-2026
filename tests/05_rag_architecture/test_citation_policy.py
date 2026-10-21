import pytest

from shared.testing import load_challenge

citation_policy = load_challenge(
    "05_rag_architecture", "citation_policy.py"
).citation_policy


def test_internal_is_optional() -> None:
    assert citation_policy(False, 0) == "optional"
    assert citation_policy(False, 4) == "optional"


def test_user_facing() -> None:
    assert citation_policy(True, 0) == "abstain_or_disclose_ungrounded"
    assert citation_policy(True, 3) == "cite_sources"


def test_negative_count() -> None:
    with pytest.raises(ValueError):
        citation_policy(True, -1)
