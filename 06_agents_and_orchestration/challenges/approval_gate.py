"""
Challenge: Approval Gate
Module 06: Agents and Orchestration

Implement the function(s) below. Run tests with:
    pytest tests/06_agents_and_orchestration/ -v
"""

def approval_gate(side_effect: str, prod: bool, amount_usd: float) -> bool:
    """
    Return True when a human must approve before the tool runs.

    Raise ValueError if side_effect is not read/write/irreversible
    or amount_usd < 0.

    read -> False
    irreversible -> True
    write -> True when (prod and amount_usd >= 1000) or amount_usd >= 10000
    otherwise False
    """
    pass
