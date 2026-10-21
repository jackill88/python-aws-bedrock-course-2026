# Reliability Cost Ops Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** Groundedness below target, with availability and latency healthy, is:

- A) `met`
- B) `quality_breach`
- C) `availability_breach`
- D) `multi_breach`

**2.** A miss on both groundedness and p95 is:

- A) `quality_breach`
- B) `latency_breach`
- C) `multi_breach`
- D) `met` if HTTP status was 200

**3.** A policy abstain inside the citation rules counts as:

- A) An availability failure
- B) A deliberate outcome, tracked separately as answer rate
- C) A throttle
- D) A cache write

**4.** A latency-sensitive steady rate of 2 rps with a peak within 1.5× is:

- A) `batch`
- B) `provisioned`
- C) `on_demand`
- D) `provisioned_with_burst_buffer`

**5.** The same steady rate with a much higher peak is:

- A) `provisioned_with_burst_buffer`
- B) `batch`
- C) `on_demand` always
- D) `met`

**6.** An async backfill that is not latency-sensitive is:

- A) `provisioned`
- B) `batch`
- C) `on_demand`
- D) `multi_breach`

**7.** Cache tokens in `token_cost_usd` are:

- A) Added on top of the same tokens also passed as `input_tokens`
- B) A separate meter. The caller does not double-count them as input
- C) Free
- D) Priced as output

**8.** Prices in that function are:

- A) USD per token
- B) USD per million tokens
- C) USD per request regardless of size
- D) A monthly commit only

**9.** The first mitigation for a bad prompt release is:

- A) Rewrite it during the incident bridge
- B) Pin the previous known-good version
- C) Disable IAM
- D) Turn temperature to 1

**10.** Fallback capacity must be:

- A) Assumed to share the primary quota
- B) Measured on the fallback model id before you promise it
- C) Unlimited because it is a fallback
- D) Hidden from the dashboard to reduce noise

## Answers

1. B  2. C  3. B  4. B  5. A  6. B  7. B  8. B  9. B  10. B
