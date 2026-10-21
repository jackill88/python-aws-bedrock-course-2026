# Cost Architecture

The bill is a set of meters. Architects who track only "the model" miss cache writes, embeddings, rerank, the vector store's floor cost, and log storage of full prompts.

## Token math

`token_cost_usd` prices four meters. **Cache tokens are not also included in `input_tokens`.** The caller splits them. Prices are USD per **million** tokens, keys `input`, `output`, `cache_read`, `cache_write`.

```python
def token_cost_usd(input_tokens, output_tokens, cache_read_tokens, cache_write_tokens, prices) -> float:
    needed = ("input", "output", "cache_read", "cache_write")
    if any(key not in prices for key in needed):
        raise ValueError("missing price")
    counts = (input_tokens, output_tokens, cache_read_tokens, cache_write_tokens)
    if any(n < 0 for n in counts):
        raise ValueError("negative tokens")
    million = 1_000_000
    return (
        input_tokens / million * prices["input"]
        + output_tokens / million * prices["output"]
        + cache_read_tokens / million * prices["cache_read"]
        + cache_write_tokens / million * prices["cache_write"]
    )
```

Confirm live prices before a budget meeting. The function's job is to make the split honest. A spreadsheet that multiplies "average tokens" by the output price for the whole prompt will not match the invoice.

## Other lines

| Line | Owner | Note |
|------|-------|------|
| Embeddings at ingest and at query | RAG platform | Re-embed is a migration cost, not an incident |
| Rerank | RAG platform | Per query, grows with top-k |
| OpenSearch OCUs, Aurora, or other index | Data platform | Floor cost even at zero queries |
| Provisioned model units | Platform | Paid while idle. Allocate them to products |
| Batch discount | Product | Only the async path |
| Invocation log storage | Security | Full prompt logging can dominate a chatty internal tool |
| Cross-AZ or cross-region data | Platform | Profile destinations are not free in the design even when the token price looks identical |

## Per-tenant controls

- Max input tokens and max output tokens per request
- Daily USD ceiling per tenant, enforced at the gateway from the same formula
- Alert at 50% and 80% of the ceiling, page at 100% with load shed
- A monthly showback so a team sees its own agent loop, not a shared mystery

Review line: **"Showback by use case and tenant. A single Bedrock line item cannot be optimized."**

A cache that never hits is a write premium you did not need (Module 03). Track hit rate next to the dollar figure.
