# Module 03: Inference Architecture

The runtime contract is where lead-architect designs become operational: which API you standardize on, how streaming fails, how tokens are budgeted, and which errors are safe to retry.

## Learning Objectives

By the end of this module you will be able to:

- Standardize generation on the Converse API and keep InvokeModel for embeddings and special payloads
- Bound a request with timeouts, output caps, and a token budget that drops retrieval before history and never drops the system prompt silently
- Decide when a stable prefix is worth prompt caching
- Retry throttles, and refuse to retry a non-idempotent call after a timeout

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | The Converse Contract | [theory/01_converse_contract.md](theory/01_converse_contract.md) |
| 2 | Streaming, Timeouts, and Partial Failure | [theory/02_streaming_timeouts_partial_failure.md](theory/02_streaming_timeouts_partial_failure.md) |
| 3 | Tokens, Caching, and Budgets | [theory/03_tokens_caching_budgets.md](theory/03_tokens_caching_budgets.md) |
| 4 | Throttling, Retries, and Backpressure | [theory/04_throttling_retries_backpressure.md](theory/04_throttling_retries_backpressure.md) |

## Quiz

Test your understanding: [quizzes/inference_architecture_quiz.md](quizzes/inference_architecture_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Retry Decision | [challenges/retry_decision.py](challenges/retry_decision.py) |
| Fit Token Budget | [challenges/fit_token_budget.py](challenges/fit_token_budget.py) |
| Cache Decision | [challenges/cache_decision.py](challenges/cache_decision.py) |

Run tests for this module:

```bash
pytest tests/03_inference_architecture/ -v
```
