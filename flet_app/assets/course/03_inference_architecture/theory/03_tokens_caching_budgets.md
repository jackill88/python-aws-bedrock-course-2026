# Tokens, Caching, and Budgets

Every request spends a context window that is also a bill. The architect's job is to decide **what is dropped first** when the sum does not fit, and **what is stable enough** to cache.

## Budget order

Reserve output first. The system prompt is not optional. If those two already exceed the limit, the request is invalid — do not silently truncate the policy text.

Then spend the remainder on history and retrieval. When they overflow, **drop retrieval tokens first** (shrink or remove the retrieved context) and only then drop history, oldest first. Dropping the system prompt to "make it fit" is how a safety policy disappears under load.

`fit_token_budget` returns a plan:

| Key | Meaning |
|-----|---------|
| `fits` | True only when nothing was dropped |
| `drop_retrieval` | How many retrieval tokens to remove |
| `drop_history` | How many history tokens to remove after retrieval is exhausted |

```python
def fit_token_budget(limit, system_tokens, history_tokens, retrieval_tokens, output_reserve):
    if min(limit, system_tokens, history_tokens, retrieval_tokens, output_reserve) < 0:
        raise ValueError("negative token count")
    if system_tokens + output_reserve > limit:
        raise ValueError("system and output reserve exceed the window")
    overflow = max(0, system_tokens + history_tokens + retrieval_tokens + output_reserve - limit)
    drop_retrieval = min(retrieval_tokens, overflow)
    drop_history = overflow - drop_retrieval
    return {
        "fits": overflow == 0,
        "drop_retrieval": drop_retrieval,
        "drop_history": drop_history,
    }
```

A plan with `fits=False` is still actionable: the caller trims, then sends. It is not permission to skip the system prompt.

## Prompt caching

Some Bedrock models accept a cache checkpoint on a **stable prefix** (system prompt, tool definitions, long standing instructions). Cache writes cost more than a normal input token; cache reads cost much less. The minimum cacheable size is **model-specific**. This course uses a teaching threshold, not a vendor constant:

- Prefix must be **stable** across calls. Personalized or tenant-specific text in the prefix defeats the cache and can cross tenants if you are careless
- Prefix length at least **1,024** tokens in this exercise
- Expected identical reuse at least **5 times per hour**, or the write premium is not worth it

`cache_decision` returns `"cache"` or `"skip"` using exactly those three gates. Negative counts raise `ValueError`.

Review line: **"Cache the instructions. Do not cache the user's secret into a shared prefix."**

## What you measure

Log input tokens, output tokens, cache read tokens, and cache write tokens separately. A cache that never hits is a silent price increase. A cache key that includes user content is a data-isolation bug.
