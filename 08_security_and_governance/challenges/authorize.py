"""
Challenge: Authorize
Module 08: Security and Governance

Implement the function(s) below. Run tests with:
    pytest tests/08_security_and_governance/ -v
"""

def authorize(role: str, action: str) -> str:
    """
    Return "allow" or "deny".

    Roles: platform_admin, app_runtime, data_scientist, auditor, product_dev.
    Actions: invoke_prod, invoke_dev, create_guardrail, read_invocation_logs,
             manage_provisioned_throughput, retrieve_kb.
    Unknown role or action -> ValueError.

    platform_admin: every action.
    app_runtime: invoke_prod, retrieve_kb.
    data_scientist: invoke_dev, read_invocation_logs.
    auditor: read_invocation_logs.
    product_dev: invoke_dev.
    Any other pair: "deny".
    """
    pass
