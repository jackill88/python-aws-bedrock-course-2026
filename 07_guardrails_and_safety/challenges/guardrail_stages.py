"""
Challenge: Guardrail Stages
Module 07: Guardrails and Safety

Implement the function(s) below. Run tests with:
    pytest tests/07_guardrails_and_safety/ -v
"""

def guardrail_stages(surface: str) -> list[str]:
    """
    Return a new list of stages.

    user_chat -> ["input", "output"]
    tool_arguments -> ["input"]
    final_answer_with_sources -> ["output", "grounding"]
    batch_generation -> ["output"]

    Raise ValueError for any other surface.
    """
    pass
