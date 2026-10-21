# Enterprise Knowledge Assistant

The common case: employees ask questions against a policy or product corpus. The wrong design is a frontier model with the share drive pasted into the prompt. The reference pattern is `managed_kb_rag`.

## Shape

```
Identity-aware gateway
  → Knowledge Base retrieve (tenant or group filter injected here)
  → optional rerank
  → token budget
  → Converse on the balanced tier, guardrail version pinned
  → grounding check
  → cite, or abstain
```

`case_pattern("hr_policy_qa")` returns `managed_kb_rag`.

| Choice | Why |
|--------|-----|
| Managed knowledge base | Sync, chunking, and citations are the product unless a requirement forces a custom index |
| Balanced tier | Answers need to follow passages, not discover new science |
| Hierarchical chunks for policy PDFs | Module 05 |
| User-facing citation policy | No passage, no claim |
| Logical or strong isolation | Employee data is rarely "public." Group ACLs inside a tenant still need a filter the model cannot skip |

## Latency budget

`latency_budget(total_ms)` splits a user-visible budget for this RAG shape. `total_ms < 100` raises `ValueError` — that is not a budget for retrieve plus generate. Percentages are integer math; the remainder goes to time-to-first-token so the parts sum to the total.

| Slice | Percent |
|-------|---------|
| `retrieval` | 15 |
| `rerank` | 10 |
| `model_ttft` | 35, plus any remainder |
| `generation_buffer` | 25 |
| `guardrails` | 15 |

```python
def latency_budget(total_ms: int) -> dict:
    if total_ms < 100:
        raise ValueError("unrealistic budget")
    parts = {
        "retrieval": 15,
        "rerank": 10,
        "model_ttft": 35,
        "generation_buffer": 25,
        "guardrails": 15,
    }
    alloc = {name: total_ms * percent // 100 for name, percent in parts.items()}
    alloc["model_ttft"] += total_ms - sum(alloc.values())
    return alloc
```

For a 2,000 ms budget: retrieval 300, rerank 200, model_ttft 700, generation_buffer 500, guardrails 300. Streaming spends the generation buffer while the user reads. It does not allow retrieval to consume the whole 2,000 ms.

If rerank does not earn its 10% on the eval set, take it out and give the time back to retrieval or to a tighter answer. The split is the default you deviate from with evidence.

Review line: **"A 2-second promise with an unbounded search is not a promise."**
