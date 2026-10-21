"""
Challenge: Abstraction Boundary
Module 02: Model Strategy

Implement the function(s) below. Run tests with:
    pytest tests/02_model_strategy/ -v
"""


def abstraction_boundary(component: str) -> str:
    """
    Return where a change is allowed to live.

    model_id -> config
    prompt_template -> versioned_artifact
    tool_schema -> contract
    business_policy -> application

    Raise ValueError for any other component.
    """
    pass
