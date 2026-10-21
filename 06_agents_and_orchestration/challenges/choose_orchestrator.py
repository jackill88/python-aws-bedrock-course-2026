"""
Challenge: Choose Orchestrator
Module 06: Agents and Orchestration

Implement the function(s) below. Run tests with:
    pytest tests/06_agents_and_orchestration/ -v
"""

def choose_orchestrator(determinism: str, tool_risk: str, open_ended: bool) -> str:
    """
    Return "workflow_with_human_approval", "workflow", "agent", or "hybrid".

    determinism: "strict" or "flexible". Else ValueError.
    tool_risk: "read", "write", or "irreversible". Else ValueError.

    Order:
    1. irreversible -> workflow_with_human_approval
    2. strict -> workflow
    3. open_ended and read -> agent
    4. open_ended and write -> hybrid
    5. otherwise -> workflow
    """
    pass
