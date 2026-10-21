"""
Challenge: Tenancy Model
Module 11: System Design

Implement the function(s) below. Run tests with:
    pytest tests/11_system_design/ -v
"""

def tenancy_model(isolation: str, tenants: int) -> str:
    """
    Raise ValueError if tenants < 1 or isolation is unknown.

    regulatory -> account_per_tenant
    strong -> index_per_tenant
    logical -> shared_index_metadata_filter

    tenants does not change the result once it is >= 1.
    """
    pass
