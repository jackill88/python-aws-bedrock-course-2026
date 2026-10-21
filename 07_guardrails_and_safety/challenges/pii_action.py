"""
Challenge: PII Action
Module 07: Guardrails and Safety

Implement the function(s) below. Run tests with:
    pytest tests/07_guardrails_and_safety/ -v
"""

def pii_action(entity: str, audience: str) -> str:
    """
    Return "allow", "mask", "block", or "redact".

    entity: email, ssn, name, phone
    audience: internal_support, external_user, logs
    Else ValueError.

    logs -> redact for every entity
    ssn + external_user -> block
    ssn + internal_support -> mask
    name + internal_support -> allow
    name + external_user -> mask
    email or phone, other than logs -> mask
    """
    pass
