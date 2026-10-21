"""
Challenge: Platform Timeout
Module 12: Lambda and ECS

Implement the function(s) below. Run tests with:
    pytest tests/12_lambda_and_ecs/ -v
"""


def platform_timeout_s(edge: str) -> int | None:
    """
    Return the platform ceiling in seconds, or None if there is no platform cap.

    api_gateway -> 29
    lambda_function_url -> 900
    alb -> 4000
    ecs_task -> None

    Else ValueError.
    """
    pass
