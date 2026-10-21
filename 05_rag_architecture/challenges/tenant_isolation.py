"""
Challenge: Tenant Isolation
Module 05: RAG Architecture

Implement the function(s) below. Run tests with:
    pytest tests/05_rag_architecture/ -v
"""


def tenant_isolation(regulatory: str, tenant_count: int) -> str:
    """
    Return the isolation level. tenant_count does not weaken the class.

    Raise ValueError if tenant_count < 1 or regulatory is unknown.

    regulated_plus -> account_per_tenant
    strict -> index_per_tenant
    standard -> shared_index_metadata_filter
    """
    pass
