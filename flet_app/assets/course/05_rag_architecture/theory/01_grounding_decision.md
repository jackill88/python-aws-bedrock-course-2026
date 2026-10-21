# The Grounding Decision

Fine-tuning memorizes behavior poorly and facts worse. Long context pastes a corpus into every call. RAG fetches a small set of passages at request time. Most production knowledge assistants are RAG. The architect's job is to notice the cases that are not.

## Inputs

| Input | Values in this course |
|-------|------------------------|
| `change_rate` | `rare`, `weekly`, `daily_or_faster` |
| `corpus_tokens` | Size of the knowledge you would otherwise paste |
| `context_budget` | Tokens you are willing to spend on that knowledge per call, after system prompt and output reserve |
| `labeled_examples` | Supervised pairs you actually have, not "we could label some" |
| `need_behavior_change` | True when the gap is style, format, or policy tone, not missing facts |

`weekly` and `daily_or_faster` are volatile knowledge. You will not retrain on that cadence.

## The order

```python
def choose_grounding(change_rate, corpus_tokens, context_budget, labeled_examples, need_behavior_change):
    if change_rate not in {"rare", "weekly", "daily_or_faster"}:
        raise ValueError("unknown change rate")
    if min(corpus_tokens, context_budget, labeled_examples) < 0:
        raise ValueError("negative size")
    volatile = change_rate in {"weekly", "daily_or_faster"}
    fits = corpus_tokens <= context_budget
    behavior = need_behavior_change and labeled_examples >= 500

    if volatile and behavior:
        return "rag_plus_finetune"
    if volatile or not fits:
        if (not volatile) and corpus_tokens <= 200_000:
            return "long_context"
        return "rag"
    if behavior:
        return "finetune"
    return "prompt_only"
```

Read it as a sequence:

1. Facts move and you also need a behavior change backed by 500+ labels → **RAG plus fine-tune**. Fine-tune does not carry the changing facts.
2. Facts move, or the corpus does not fit the budget → retrieval, except the narrow long-context case.
3. Long context only when facts are **rare**-changing, the corpus does **not** fit the budget, and it is still within **200,000** tokens. You accept the input-token bill. Above that, RAG.
4. Facts are rare, they fit in the budget, and behavior needs a real labeled set → **fine-tune**.
5. Facts are rare, they fit, and you do not need a behavior shift → **prompt only**.

Review line: **"Fine-tune for stable behavior. Retrieve for knowledge you would not swear is in the weights."**

## Worked cases

| Situation | Result |
|-----------|--------|
| Hourly price list, no behavior project | `rag` |
| Hourly price list, and 2,000 labeled tone examples | `rag_plus_finetune` |
| A 120k-token handbook that changes yearly, budget 8k | `long_context` |
| A 500k-token handbook, rare changes, budget 8k | `rag` |
| A 2k-token policy, rare changes, 800 labeled rewrites of the house style | `finetune` |
| A 2k-token policy, rare changes, no behavior project | `prompt_only` |

200,000 is a teaching ceiling for "stuff it anyway," not a promise about any one model's window. Windows move. The cost and the lost-in-the-middle problem do not.
