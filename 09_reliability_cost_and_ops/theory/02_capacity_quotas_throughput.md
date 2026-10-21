# Capacity, Quotas, and Throughput

On-demand Bedrock is quota-shaped: requests per minute and tokens per minute, per model, per region, raised through Service Quotas with a lead time. Provisioned throughput is a commitment of model units so that steady interactive traffic does not live on leftovers. Batch is a different queue.

## The plan

`capacity_plan(p95_latency_sensitive, steady_rps, peak_rps, async_backfill)`:

| Order | Result |
|-------|--------|
| `steady_rps < 0`, `peak_rps < 0`, or `peak_rps < steady_rps` | `ValueError` |
| Async backfill and not latency-sensitive | `batch` |
| Latency-sensitive and `steady_rps >= 2`, and peak is within 1.5× steady | `provisioned` |
| Latency-sensitive and `steady_rps >= 2`, and peak is above 1.5× steady | `provisioned_with_burst_buffer` |
| Otherwise | `on_demand` |

```python
def capacity_plan(p95_latency_sensitive, steady_rps, peak_rps, async_backfill) -> str:
    if steady_rps < 0 or peak_rps < 0 or peak_rps < steady_rps:
        raise ValueError("inconsistent rates")
    if async_backfill and not p95_latency_sensitive:
        return "batch"
    if p95_latency_sensitive and steady_rps >= 2:
        if peak_rps <= steady_rps * 1.5:
            return "provisioned"
        return "provisioned_with_burst_buffer"
    return "on_demand"
```

The 2 requests/second steady floor is a teaching stand-in for "large enough that a commit beats surprise throttling." Replace it with a quote, but do not skip the comparison. Burst buffer means you buy provisioned capacity for the steady load and you still have a story for the peak: a queue, a second region you already approved, or a short on-demand overflow that is itself quota-checked. "Burst" is not permission to ignore the peak.

## Load tests

Test the model id, the region, and the fallback id. Record tokens per minute, not only requests. A traffic test of 100-token prompts says nothing about a 20k-token RAG prompt. Include the guardrail and the retriever; they consume the user-visible latency budget even when the model quota is fine.

Quota increases have a calendar. A launch date that assumes a same-week TPM increase is a hope. Provisioned throughput also has a purchasing lead time. Put both on the plan next to the feature flag.

Review line: **"The fallback model has its own quota. Measure it before you promise failover."**
