# Agents Orchestration Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** An irreversible tool on an open-ended task maps to:

- A) `agent`
- B) `workflow_with_human_approval`
- C) `hybrid`
- D) `workflow` with no human

**2.** Strict determinism and a read tool, even if the task is open-ended, maps to:

- A) `agent`
- B) `workflow`
- C) `hybrid`
- D) `workflow_with_human_approval`

**3.** A flexible, open-ended task whose tools only read maps to:

- A) `agent`
- B) `workflow`
- C) `hybrid`
- D) `finetune`

**4.** A flexible, open-ended task that writes maps to:

- A) `agent`
- B) `hybrid`
- C) `prompt_only`
- D) `workflow_with_human_approval` automatically, even when the write is reversible and small

**5.** Idempotency keys are required for:

- A) Every read
- B) Writes and irreversible actions
- C) Embedding calls only
- D) CloudTrail

**6.** Who mints the idempotency key?

- A) The model, freshly, on each retry
- B) The gateway, once per user action
- C) The foundation-model vendor
- D) The vector index

**7.** `approval_gate("write", prod=True, amount_usd=1000)` is:

- A) False
- B) True
- C) A `ValueError`
- D) Only true outside prod

**8.** `approval_gate("read", prod=True, amount_usd=50000)` is:

- A) True
- B) False
- C) `irreversible`
- D) `hybrid`

**9.** A sentence in the chat that says the user agreed is:

- A) An approval record
- B) Not an approval. Approval binds the tool arguments in a workflow the model cannot edit afterward
- C) Sufficient for irreversible tools
- D) A Step Functions state by itself

**10.** Durable order status belongs in:

- A) The conversation transcript
- B) The system of record the tool writes
- C) The system prompt
- D) The cache prefix shared across tenants

## Answers

1. B  2. B  3. A  4. B  5. B  6. B  7. B  8. B  9. B  10. B
