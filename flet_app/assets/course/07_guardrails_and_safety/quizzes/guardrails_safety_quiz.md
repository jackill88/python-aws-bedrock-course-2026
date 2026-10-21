# Guardrails Safety Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** Tool arguments should be checked as:

- A) A grounding stage only
- B) An input stage before the tool runs
- C) Something the model has already made safe
- D) A control-plane list call

**2.** A user-facing grounded answer runs:

- A) `output` and `grounding`
- B) `input` only
- C) No stages, because retrieval already happened
- D) `batch` only

**3.** Production should pin:

- A) The guardrail draft
- B) A guardrail version, the same way it pins a prompt
- C) Whatever was last edited in the console
- D) No guardrail identifier

**4.** Logs should treat email, SSN, phone, and name as:

- A) `allow`
- B) `redact`
- C) `block` the entire logging pipeline
- D) `mask` for SSN only, allow the rest

**5.** An SSN in a reply to an external user is:

- A) `mask`
- B) `block`
- C) `allow`
- D) `redact` in the UI and allow in the API

**6.** An internal support view of a customer name is:

- A) `allow`
- B) `block`
- C) `redact` always
- D) `ValueError`

**7.** Zero factual claims in the answer yields grounding verdict:

- A) `fail`, because the ratio is undefined
- B) `pass`
- C) `block`
- D) `retry`

**8.** 9 supported claims out of 10, with `min_ratio` 0.95, is:

- A) `pass`
- B) `fail`
- C) `pass` if the content filter is off
- D) `ValueError`

**9.** A guardrail is a sufficient replacement for tenant filters and tool authorization:

- A) Yes, if the denied-topic list is long
- B) No. Those controls stay in the gateway and the tool
- C) Only for batch
- D) Only when using a frontier model

**10.** On a grounding failure at runtime you should:

- A) Show the draft so the user can decide
- B) Abstain, and not run an unbounded "try harder" retry loop
- C) Disable the guardrail for the tenant
- D) Fine-tune immediately

## Answers

1. B  2. A  3. B  4. B  5. B  6. A  7. B  8. B  9. B  10. B
