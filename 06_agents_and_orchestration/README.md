# Module 06: Agents and Orchestration

An agent is a loop that picks tools until it stops. A workflow is a graph you can draw before the request arrives. Lead architects choose the loop only when the path is genuinely open-ended, and they take write tools back out of it.

## Learning Objectives

By the end of this module you will be able to:

- Choose a workflow, an agent, a hybrid, or a human-approval workflow from determinism and tool risk
- Require an idempotency key on every write tool
- Place approval on irreversible actions and on large production writes
- Keep multi-agent designs auditable instead of merely impressive

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Agent Loop versus Workflow | [theory/01_agent_vs_workflow.md](theory/01_agent_vs_workflow.md) |
| 2 | Tool Contracts and Side Effects | [theory/02_tool_contracts_and_side_effects.md](theory/02_tool_contracts_and_side_effects.md) |
| 3 | Human Approval and Blast Radius | [theory/03_human_approval_and_blast_radius.md](theory/03_human_approval_and_blast_radius.md) |
| 4 | Multi-Agent Systems and State | [theory/04_multi_agent_and_state.md](theory/04_multi_agent_and_state.md) |

## Quiz

Test your understanding: [quizzes/agents_orchestration_quiz.md](quizzes/agents_orchestration_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Choose Orchestrator | [challenges/choose_orchestrator.py](challenges/choose_orchestrator.py) |
| Approval Gate | [challenges/approval_gate.py](challenges/approval_gate.py) |
| Tool Idempotency Key | [challenges/tool_idempotency_key.py](challenges/tool_idempotency_key.py) |

Run tests for this module:

```bash
pytest tests/06_agents_and_orchestration/ -v
```
