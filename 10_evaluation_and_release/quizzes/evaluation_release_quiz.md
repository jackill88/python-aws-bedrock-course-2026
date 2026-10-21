# Evaluation Release Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** Recall at 3 for retrieved `[a, b, a]` and relevant `{a, c}` is:

- A) 1.0
- B) 0.5
- C) 0.0
- D) Undefined because of the duplicate

**2.** An empty relevant set should:

- A) Return 0
- B) Raise `ValueError`
- C) Return 1
- D) Skip the case silently inside the metric function

**3.** Format compliance should be judged by:

- A) A human panel only
- B) An automatic parser
- C) The same model that generated the text, with no audit
- D) Thumbs-down in production only

**4.** Helpfulness should be judged by:

- A) `human_sample`
- B) `automatic_ok`
- C) Token count
- D) The guardrail trace alone

**5.** Policy-violation flags should:

- A) Auto-ship when the flag is clear
- B) Use automation plus a human on positives
- C) Be ignored if groundedness passed
- D) Replace IAM

**6.** A grounding judge must:

- A) See the source passages, and itself be audited on a sample
- B) Score fluency with no sources
- C) Be the candidate model
- D) Run only in production

**7.** `release_decision` when safety fails and offline is 0.99:

- A) `ship`
- B) `block`
- C) `ship` if cost fell
- D) `ValueError`

**8.** A shadow delta of `-0.03` with safety passing and a strong offline score:

- A) `ship`
- B) `block`
- C) `ship` because 0.03 is small
- D) `automatic_ok`

**9.** A 40% cost increase with a shadow quality delta of `0.01`:

- A) `ship`, because quality did not fall
- B) `block`
- C) `ship` if offline is 0.8
- D) Always `ValueError`

**10.** A 40% cost increase with a shadow quality delta of `0.05` and otherwise healthy gates:

- A) `block`
- B) `ship`
- C) `block` because any cost increase blocks
- D) `human_sample` as the return value

## Answers

1. B  2. B  3. B  4. A  5. B  6. A  7. B  8. B  9. B  10. B
