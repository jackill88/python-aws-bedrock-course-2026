import pytest

from shared.testing import load_challenge

trust_zone = load_challenge("04_prompt_systems", "trust_zone.py").trust_zone


@pytest.mark.parametrize("source", ["system_prompt", "developer"])
def test_trusted(source: str) -> None:
    assert trust_zone(source) == "trusted"


def test_semi_trusted_schema() -> None:
    assert trust_zone("tool_schema") == "semi_trusted"


@pytest.mark.parametrize(
    "source",
    ["user_message", "retrieved_chunk", "tool_result", "uploaded_file"],
)
def test_untrusted(source: str) -> None:
    assert trust_zone(source) == "untrusted"


def test_unknown_source() -> None:
    with pytest.raises(ValueError):
        trust_zone("wiki_pasted_into_schema")
