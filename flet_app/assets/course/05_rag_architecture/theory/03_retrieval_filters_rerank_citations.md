# Retrieval, Filters, Rerank, Citations

A retrieve call returns passages. It does not return permission to speak. The gateway filters, optionally reranks, and the answer path cites or abstains.

## The path

```
query
  → embed with the same model used at ingest
  → vector search + keyword search (hybrid) where the index supports it
  → metadata filter (tenant, acl, effective date) in the query, not after the model
  → optional rerank on the top candidates
  → pack into the token budget (Module 03)
  → Converse
  → grounding check and citations (Module 07)
```

`Retrieve` plus your own `Converse` call is the lead-architect default when citations, eval, and tenancy matter. `RetrieveAndGenerate` is acceptable for a low-risk internal tool where the managed prompt is good enough and you still cannot skip the filter.

Hybrid search matters when users type identifiers, error codes, and exact policy names. Pure vector search paraphrases well and misses exact tokens. Rerank (a cross-encoder such as a Bedrock rerank model) is a quality spend on the top N, not a reason to retrieve the whole corpus.

## Citations

`citation_policy(user_facing, retrieved_count)`:

| Condition | Result |
|-----------|--------|
| `retrieved_count < 0` | `ValueError` |
| Not user-facing | `optional` |
| User-facing and nothing retrieved | `abstain_or_disclose_ungrounded` |
| User-facing and at least one passage | `cite_sources` |

An internal classifier may skip citations. A user-facing policy assistant may not answer from parametric memory and pretend it used the handbook. If retrieval returns nothing, the product says it does not know or that the answer is ungrounded. It does not fill the gap with a fluent guess.

Review line: **"No passage, no claim. A citation the user cannot open is decoration."**

Store the passage ids on the trace. The citation in the UI should resolve to a source URI and, when you have it, a page or section. "Source: document" is not an audit trail.

## Failure modes

| Symptom | Likely cause |
|---------|----------------|
| Confident, wrong, with a citation | The chunk itself is stale or the model over-claimed beyond it. Grounding check |
| Right document, wrong tenant | Filter not enforced in the gateway |
| Exact error code not found | Vector-only search |
| Answer ignores the best paragraph | Chunk too large, or the relevant span lost its header |
| Cost spike | Top-k too high, rerank on every keystroke, no cache of repeated queries |
