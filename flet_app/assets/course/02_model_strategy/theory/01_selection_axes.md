# Selection Axes

A model review that starts with a logo ends with a surprise bill or a missed SLO. Start with the **task**, the **latency class**, and whether the call must **use tools**. Quality, context length, modality, residency, and price are constraints on that choice — not a single score.

## Tiers, not brand names

This course uses three tiers so the architecture survives a model rename:

| Tier | Shape | Typical job |
|------|-------|-------------|
| **small** | Cheap, fast | Classification, extraction, routing, short summaries |
| **balanced** | Default production quality | RAG answers, tool use, most user-facing text |
| **frontier** | Highest reasoning cost | Hard multi-step reasoning, ambiguous policy, cases where a wrong answer is expensive and a slower one is acceptable |

Real catalogs (Claude, Nova, Llama, Mistral, and others) move inside these tiers. The gateway config maps a tier to a model id **per region**. Application code asks for a tier or a use-case name.

## The rule for this course

`select_model_tier(task, latency_class, needs_tools)` returns `small`, `balanced`, or `frontier`.

| Task | Result before the tool upgrade |
|------|--------------------------------|
| `complex_reasoning` | `frontier` |
| `agent` | `balanced` |
| `rag_answer` | `balanced` |
| `classify` or `extract` | `small` |

`latency_class` is `"interactive"` or `"batch"`. It does **not** by itself change the tier in this exercise. Batch saves money through the batch API (Module 01), not by silently dropping a RAG answer onto a weaker model. A cheaper batch tier is a separate decision with its own eval.

After the table, apply one upgrade: if `needs_tools` is true and the tier would have been `small`, return `balanced`. Frontier stays frontier. Tool use wants a model that follows a schema reliably.

```python
def select_model_tier(task: str, latency_class: str, needs_tools: bool) -> str:
    if latency_class not in {"interactive", "batch"}:
        raise ValueError("unknown latency class")
    table = {
        "complex_reasoning": "frontier",
        "agent": "balanced",
        "rag_answer": "balanced",
        "classify": "small",
        "extract": "small",
    }
    if task not in table:
        raise ValueError("unknown task")
    tier = table[task]
    if needs_tools and tier == "small":
        tier = "balanced"
    return tier
```

## Axes you still write down

| Axis | Architect's question |
|------|----------------------|
| Quality bar | What failure is unacceptable? A hallucinated policy, or a terse label? |
| Latency | Time to first token, or full completion? Streaming changes the UX budget |
| Context | Do we retrieve, or do we stuff? Stuffing a frontier model is a cost decision |
| Tools | Schema fidelity matters more than prose style |
| Residency | Is this model id actually offered in the allowed regions? |
| Price | Cost per successful task, not cost per demo prompt |
| Data terms | First-party Bedrock model vs Marketplace |

Review line: **"We selected a tier for the task. The model id is configuration."**

## What not to do

- Pick the frontier model for classification so nobody has to choose
- Pick the small model for an agent because the unit price looked low, then spend the savings on retries and bad tool calls
- Compare two models on five prompts and call it an evaluation (Module 10)
