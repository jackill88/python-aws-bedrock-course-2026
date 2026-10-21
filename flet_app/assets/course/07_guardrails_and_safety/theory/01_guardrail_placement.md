# Where Guardrails Sit

A guardrail attached to `Converse` evaluates the user input, the model output, or both, and can return `guardrail_intervened`. `ApplyGuardrail` evaluates text **without** invoking a foundation model. Use that when the thing you must check is not a chat turn: tool arguments, a document before it is indexed, a batch line before it is stored.

## Surfaces in this course

`guardrail_stages(surface)` returns the stages to run, as a new list:

| Surface | Stages |
|---------|--------|
| `user_chat` | `input`, `output` |
| `tool_arguments` | `input` |
| `final_answer_with_sources` | `output`, `grounding` |
| `batch_generation` | `output` |
| Anything else | `ValueError` |

Input on a chat turn is the user text (and, when you configure it, content that must not reach the model). Output is the model's draft before the user sees it. Tool arguments are checked as **input** because they are about to become an API call; the model already produced them, but the risk is execution, so you block before the tool. Grounding is a separate stage from a generic output filter: it compares claims to the passages you supplied. Batch jobs still need the output check. Skipping it because "no one is waiting" is how a nightly file fills a warehouse with policy violations.

```python
def guardrail_stages(surface: str) -> list[str]:
    mapping = {
        "user_chat": ["input", "output"],
        "tool_arguments": ["input"],
        "final_answer_with_sources": ["output", "grounding"],
        "batch_generation": ["output"],
    }
    if surface not in mapping:
        raise ValueError("unknown surface")
    return list(mapping[surface])
```

Return a copy. Callers may append telemetry without mutating a shared constant.

## Versioning

Guardrails have a version, and a draft. Production pins a version the same way it pins a prompt (Module 04). `DRAFT` in production means this morning's console edit is live. The gateway config carries `guardrailIdentifier` and `guardrailVersion`.

Review line: **"The guardrail version is part of the release, not a side setting someone tweaks after launch."**

## What the trace is for

Enable the guardrail trace on calls you are still evaluating. The trace says which policy fired. A metric that only counts `guardrail_intervened` cannot tell a PII mask from a denied topic. Those are different products to the user and different pages for the on-call.
