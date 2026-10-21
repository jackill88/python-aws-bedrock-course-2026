# Contextual Grounding

Contextual grounding checks whether the model's claims are supported by the reference passages you provide (the retrieved chunks), and can score relevance of those passages to the question. It is the Bedrock feature that matches the citation policy in Module 05. A content filter will not notice a fluent policy answer that the handbook does not support.

## The verdict

`grounding_verdict(supported_claims, total_claims, min_ratio)`:

| Condition | Result |
|-----------|--------|
| Negative counts, `supported_claims > total_claims`, or `min_ratio` outside `[0, 1]` | `ValueError` |
| `total_claims == 0` | `pass` — the answer asserted nothing factual |
| `supported_claims / total_claims >= min_ratio` | `pass` |
| Otherwise | `fail` |

Zero claims is a pass on purpose. "I don't know" and a clarifying question are successes for a grounded assistant. Do not force a claim so the ratio is defined.

```python
def grounding_verdict(supported_claims: int, total_claims: int, min_ratio: float) -> str:
    if supported_claims < 0 or total_claims < 0 or supported_claims > total_claims:
        raise ValueError("bad claim counts")
    if not 0 <= min_ratio <= 1:
        raise ValueError("bad ratio")
    if total_claims == 0:
        return "pass"
    if supported_claims / total_claims >= min_ratio:
        return "pass"
    return "fail"
```

A typical production bar in this course's designs is **0.9 or higher** for user-facing policy answers: one unsupported claim in ten is already a lot. Lower the bar only for low-stakes summarization, and write the number in the SLO (Module 09).

## How you get the counts

The guardrail can do this inside the model call when you pass the grounding sources. You can also score offline with an eval harness (Module 10). Do not use two definitions of "supported" without noticing. The release gate and the runtime intervene path should share a threshold or document why they differ.

On `fail` at runtime: do not stream the draft to the user. Return the abstain message from the citation policy. Log the score and the passage ids. Do not automatically retry the model with "try harder" more than once; the second try often restates the same invention.

Review line: **"Grounding fails closed. A second, more creative sample is not a control."**

## What grounding does not prove

- The passages themselves may be wrong or stale. Grounding to a bad chunk is a successful check and a bad answer. Freshness is an ingestion SLO.
- The check does not prove tenancy. A perfectly grounded answer from another tenant's document is an incident.
- Relevance of retrieved text and support of the answer are different scores. High relevance with an over-claimed sentence still fails the claim ratio.
