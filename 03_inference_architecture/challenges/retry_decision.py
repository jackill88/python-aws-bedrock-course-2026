"""
Challenge: Retry Decision
Module 03: Inference Architecture

Implement the function(s) below. Run tests with:
    pytest tests/03_inference_architecture/ -v
"""


def retry_decision(
    error_code: str,
    attempt: int,
    max_attempts: int,
    idempotent: bool,
) -> str:
    """
    Return "retry" or "fail".

    attempt is the 1-based attempt that just failed.
    max_attempts is the maximum number of tries.

    Raise ValueError if attempt < 1 or max_attempts < 1.

    ValidationException and AccessDeniedException -> "fail".
    Unknown error codes -> ValueError.
    If attempt >= max_attempts -> "fail".
    ThrottlingException with attempts remaining -> "retry".
    ModelTimeoutException, InternalServerException, ServiceUnavailableException
        -> "retry" only when idempotent, else "fail".
    """
    pass
