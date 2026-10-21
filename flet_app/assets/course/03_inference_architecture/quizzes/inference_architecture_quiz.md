# Inference Architecture Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** Generation across several chat models should standardize on:

- A) A different JSON body per model, copied into each service
- B) `Converse`, with `InvokeModel` kept for embeddings and special payloads
- C) Only batch inference
- D) CloudTrail

**2.** `stopReason == max_tokens` means:

- A) The answer is complete and safe
- B) The answer was truncated by the output cap
- C) The guardrail approved the text
- D) The call should be retried with a larger prompt and no cap

**3.** A stalled stream should be governed by:

- A) A single infinite socket
- B) A client deadline, a shorter gateway deadline, and a stall timeout
- C) Provisioned throughput only
- D) Disabling `maxTokens`

**4.** When the window is short, drop tokens in which order?

- A) System prompt, then output reserve, then the user question
- B) Retrieval first, then history; never by shrinking the system prompt below a valid request
- C) Output reserve only
- D) Randomly, to be fair

**5.** If the system prompt plus the output reserve already exceeds the limit, `fit_token_budget` should:

- A) Drop the system prompt
- B) Raise `ValueError`
- C) Return `fits=True`
- D) Switch to batch

**6.** This course caches a prefix when it is stable, at least 1,024 tokens, and:

- A) Used at least 5 times per hour
- B) Contains the user's national id, for locality
- C) Changes every call
- D) Is shorter than 100 tokens

**7.** `ThrottlingException` on attempt 1 of 3 returns:

- A) `fail`
- B) `retry`
- C) `ValueError`
- D) `fallback_model` from this function

**8.** `ModelTimeoutException` with `idempotent=False` and attempts remaining returns:

- A) `retry`
- B) `fail`
- C) `cache`
- D) `provisioned`

**9.** `ValidationException` with attempts remaining returns:

- A) `retry`
- B) `fail`
- C) `cache`
- D) `skip`

**10.** Backpressure for interactive traffic over quota is:

- A) An unbounded in-request retry loop
- B) Shed or queue, with per-tenant limits, rather than hammering the same quota
- C) Grant the app role control-plane admin
- D) Raise temperature

## Answers

1. B  2. B  3. B  4. B  5. B  6. A  7. B  8. B  9. B  10. B
