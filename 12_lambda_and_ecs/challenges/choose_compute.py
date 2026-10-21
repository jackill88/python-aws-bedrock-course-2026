"""
Challenge: Choose Compute
Module 12: Lambda and ECS

Implement the function(s) below. Run tests with:
    pytest tests/12_lambda_and_ecs/ -v
"""


def choose_compute(pattern: str, max_duration_s: int) -> str:
    """
    Return "lambda" or "ecs_fargate".

    pattern: "event", "response_stream", or "held_session".
    Else ValueError. max_duration_s < 0 -> ValueError.

    held_session -> ecs_fargate
    max_duration_s > 900 -> ecs_fargate
    otherwise -> lambda
    """
    pass
