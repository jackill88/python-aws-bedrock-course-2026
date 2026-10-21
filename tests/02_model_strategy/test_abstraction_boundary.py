import pytest

from shared.testing import load_challenge

abstraction_boundary = load_challenge(
    "02_model_strategy", "abstraction_boundary.py"
).abstraction_boundary


@pytest.mark.parametrize(
    ("component", "boundary"),
    [
        ("model_id", "config"),
        ("prompt_template", "versioned_artifact"),
        ("tool_schema", "contract"),
        ("business_policy", "application"),
    ],
)
def test_boundaries(component: str, boundary: str) -> None:
    assert abstraction_boundary(component) == boundary


def test_unknown_component() -> None:
    with pytest.raises(ValueError):
        abstraction_boundary("logo")
