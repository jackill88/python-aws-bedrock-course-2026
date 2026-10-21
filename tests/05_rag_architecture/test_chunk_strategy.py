import pytest

from shared.testing import load_challenge

chunk_strategy = load_challenge(
    "05_rag_architecture", "chunk_strategy.py"
).chunk_strategy


@pytest.mark.parametrize(
    ("doc_type", "strategy"),
    [
        ("policy_pdf", "hierarchical"),
        ("faq", "one_chunk_per_item"),
        ("chat_log", "fixed_with_overlap"),
        ("code", "structure_aware"),
        ("scanned_form", "parse_then_fixed"),
    ],
)
def test_known_types(doc_type: str, strategy: str) -> None:
    assert chunk_strategy(doc_type) == strategy


def test_unknown_type() -> None:
    with pytest.raises(ValueError):
        chunk_strategy("podcast")
