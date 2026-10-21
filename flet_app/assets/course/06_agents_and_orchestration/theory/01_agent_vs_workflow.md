# Agent Loop versus Workflow

Bedrock Agents run a model loop: the model may call action-group tools, read a knowledge base, and decide when it is done. Step Functions, and Bedrock Flows for model-centric graphs, run a path you specified. Both can call Converse. They fail differently.

## How to choose

`choose_orchestrator(determinism, tool_risk, open_ended)`:

| Check, in order | Result |
|-----------------|--------|
| Unknown `determinism` (`strict` or `flexible` only) or unknown `tool_risk` (`read`, `write`, `irreversible`) | `ValueError` |
| `tool_risk == irreversible` | `workflow_with_human_approval` |
| `determinism == strict` | `workflow` |
| `open_ended` and `tool_risk == read` | `agent` |
| `open_ended` and `tool_risk == write` | `hybrid` |
| Anything left (flexible, but not an open-ended read or write) | `workflow` |

Irreversible wins over "but the conversation is open-ended." Strict wins over a tempting agent. A write tool on an open-ended task is a **hybrid**: the agent may plan and read; the write goes through a workflow step you can retry, audit, and approve.

```python
def choose_orchestrator(determinism, tool_risk, open_ended) -> str:
    if determinism not in {"strict", "flexible"} or tool_risk not in {"read", "write", "irreversible"}:
        raise ValueError("unknown input")
    if tool_risk == "irreversible":
        return "workflow_with_human_approval"
    if determinism == "strict":
        return "workflow"
    if open_ended and tool_risk == "read":
        return "agent"
    if open_ended and tool_risk == "write":
        return "hybrid"
    return "workflow"
```

## What each option is good at

| Option | Draw it as | Weakness |
|--------|------------|----------|
| `workflow` | States, timeouts, catch, retry | Poor when the next step depends on language you cannot enumerate |
| `agent` | A capped tool loop over read APIs and a knowledge base | Hard to certify, easy to run long, weak audit unless you trace every hop |
| `hybrid` | Agent proposes; workflow executes writes | Two runtimes to operate. Worth it when the write is real |
| `workflow_with_human_approval` | A callback task a person completes | Latency is human. Do not hide it inside a chat spinner with no status |

Review line: **"If I can draw the happy path on one whiteboard, it is a workflow. The agent is for the part I cannot draw."**

## Bedrock-shaped building blocks

| Building block | Use |
|----------------|-----|
| Converse tool use in your service | You own the loop, the cap, and the logs. Best default for a single team |
| Bedrock Agents action groups | Managed loop, OpenAPI or Lambda tools, return-of-control when your VPC must run the tool |
| Knowledge base on the agent | Retrieval without you packing chunks. You still own tenancy |
| Flows | Prompt, knowledge base, and condition nodes when the graph is model-heavy and finite |
| Step Functions | Approvals, long waits, fan-out, and anything that must exist even when the model is down |

Return of control means the agent stops and hands the proposed tool call to your process. That is the hook for approval and for tools that must not run inside a Bedrock-managed Lambda.
