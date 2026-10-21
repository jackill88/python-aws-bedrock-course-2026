# RAG and Agent Metrics

End-to-end "the answer looked nice" hides a retrieval failure inside a fluent model. Split the metrics.

## Retrieval

`recall_at_k(retrieved, relevant, k)` is the fraction of relevant ids that appear in the first `k` retrieved ids. Duplicates in the retrieved list do not count twice. `k <= 0` or an empty relevant set raises `ValueError` — an empty relevant set means the case was written wrong, not that recall is zero.

```python
def recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    if k <= 0 or not relevant:
        raise ValueError("recall is undefined")
    return len(set(retrieved[:k]) & set(relevant)) / len(relevant)
```

Recall does not measure order beyond the cutoff, and it does not measure whether the generator used the passage. Pair it with a grounding score (Module 07) on the final answer. A change that improves recall and tanks groundedness still fails the release.

Report the cutoff you will actually pack into the token budget. Recall at 50 with a budget that fits 5 passages is a vanity metric.

## Generation and tools

| Metric | Measures |
|--------|----------|
| Groundedness | Share of claims supported by the passages |
| Citation validity | The cited id was actually retrieved and supports the sentence |
| Abstain correctness | Empty retrieval led to abstain, not a guess |
| Schema pass rate | Structured output validated |
| Tool-argument accuracy | The tool would have been called with authorized, correct ids |
| Harmful tool rate | A write or irreversible tool was proposed when the policy forbids it |

For agents, log the hop count distribution. A quality win that doubles hops is a cost and latency change, and the release gate treats unjustified cost as a block.

Review line: **"Ship retrieval metrics and answer metrics. One blended score will hide the regression you most need to see."**
