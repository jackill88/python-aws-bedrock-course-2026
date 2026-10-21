"""
Challenge: Fallback Route
Module 02: Model Strategy

Implement the function(s) below. Run tests with:
    pytest tests/02_model_strategy/ -v
"""


def fallback_route(error_code: str) -> str:
    """
    Return "same_model_backoff", "fallback_model", or "fail_closed".

    same_model_backoff:
        ThrottlingException, ServiceQuotaExceededException
    fallback_model:
        ModelTimeoutException, ModelErrorException, InternalServerException
    fail_closed:
        ValidationException, AccessDeniedException

    Raise ValueError for any other error code.
    """
    pass
