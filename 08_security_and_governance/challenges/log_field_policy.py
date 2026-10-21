"""
Challenge: Log Field Policy
Module 08: Security and Governance

Implement the function(s) below. Run tests with:
    pytest tests/08_security_and_governance/ -v
"""

def log_field_policy(field: str) -> str:
    """
    request_id, model_id, latency_ms, token_counts -> keep
    prompt, completion, retrieved_text -> redact_or_separate_restricted_store
    api_key, authorization -> drop
    Else ValueError.
    """
    pass
