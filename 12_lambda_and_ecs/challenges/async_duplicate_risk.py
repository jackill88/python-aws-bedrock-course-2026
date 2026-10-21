"""
Challenge: Async Duplicate Risk
Module 12: Lambda and ECS

Implement the function(s) below. Run tests with:
    pytest tests/12_lambda_and_ecs/ -v
"""


def async_duplicate_risk(invoke_mode: str, side_effect: str) -> str:
    """
    Return "client_retries_only", "duplicate_model_call", or "duplicate_side_effect".

    invoke_mode: "sync" or "async". Else ValueError.
    side_effect: "read", "write", or "irreversible". Else ValueError.

    sync -> client_retries_only
    async + read -> duplicate_model_call
    async + write or irreversible -> duplicate_side_effect
    """
    pass
