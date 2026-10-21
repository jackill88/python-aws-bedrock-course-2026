# Consumption and Commercial Model

Lead architects get the commercial model wrong when they price a demo and then meet production throughput. Bedrock has three consumption shapes that answer different constraints. Prices move; **the shape of the bill** is the durable lesson. Confirm numbers on the current price card before you commit a budget.

## The three shapes

| Mode | You pay for | Latency | Idle cost | Use when |
|------|-------------|---------|-----------|----------|
| **On-demand** | Tokens (and related meters such as cache reads/writes where they apply) | Interactive, subject to quotas | None beyond usage | Spiky or low volume, or you have not earned a reserved baseline |
| **Provisioned throughput** | Reserved model capacity for a term | Predictable if you sized the units | You pay the commitment even when quiet | Steady, latency-sensitive traffic that would throttle on-demand |
| **Batch inference** | Tokens, at a lower rate than on-demand for supported models | Minutes to hours, not a user click | None beyond the job | Large async jobs: eval sets, backfills, nightly summarization |

Review line: **"Interactive SLOs do not ride the batch API. Idle provisioned throughput is a standing cost."**

A common discount story for batch is "about half of on-demand" on supported models. Treat that as a hypothesis to verify, not a constant in your spreadsheet.

## How to choose

Apply the rules in this order. They are the contract for `choose_consumption_mode`.

1. **Batch** when the work is asynchronous **and** the caller is not latency-sensitive. A user waiting on a spinner is latency-sensitive even if you wish they were not.
2. **Provisioned** when the caller is latency-sensitive, the baseline is predictable, and volume is high enough to justify a floor. In this course that threshold is **100,000 requests/day**. Below that, on-demand is the default even if traffic is steady — the commit can cost more than the tokens.
3. **On-demand** for everything else: spiky interactive traffic, low volume, prototypes, and latency-sensitive workloads that are not a steady baseline.

```python
def choose_consumption_mode(
    requests_per_day: int,
    latency_sensitive: bool,
    predictable_baseline: bool,
    async_ok: bool,
) -> str:
    if async_ok and not latency_sensitive:
        return "batch"
    if (
        latency_sensitive
        and predictable_baseline
        and requests_per_day >= 100_000
    ):
        return "provisioned"
    return "on_demand"
```

`requests_per_day < 0` is a `ValueError`. The flags are booleans; do not invent extra modes.

## Quotas sit beside the price

On-demand is not infinite. Accounts have **requests-per-minute and tokens-per-minute** quotas per model per region. A launch that "worked in dev" throttles when the real tenant arrives. Provisioned throughput is how you buy a latency story; a quota increase is how you raise the on-demand ceiling. They are different conversations with different lead times.

Load-test the **model id and region** you will pin. A fallback model has its **own** quota. Fallback that shares the same saturated quota is not fallback.

## Other meters architects forget

| Meter | When it shows up |
|-------|------------------|
| Input vs output tokens | Output is often the expensive side; long answers dominate |
| Prompt-cache write vs cache read | Stable prefixes: write premium, then cheap reads. Unstable prefixes never pay back |
| Embeddings | Ingestion and query embedding, separate from the answer model |
| Rerank | Per search, easy to omit from the RAG budget |
| Knowledge base / vector store | OpenSearch OCUs, Aurora, or a third-party index — not a Bedrock token line |
| Provisioned commit | Fixed, even at zero traffic |
| Data transfer and logs | Invocation logs of full prompts can cost more than the model on a chatty internal tool |

## Multi-tenant money

A shared on-demand account with no per-tenant budget is a single noisy neighbor away from a throttling incident and a surprise bill. The gateway should enforce:

- A token ceiling per request (input and output)
- A daily ceiling per tenant
- A kill switch that does not require redeploying the model

Provisioned throughput is a platform asset. Do not let one product team consume the reserved units of another without an explicit allocation.
