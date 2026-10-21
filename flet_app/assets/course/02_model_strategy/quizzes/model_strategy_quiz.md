# Model Strategy Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** This course maps `rag_answer` to which tier before any tool upgrade?

- A) small
- B) balanced
- C) frontier
- D) batch

**2.** `classify` with `needs_tools=True` returns:

- A) small
- B) balanced
- C) frontier
- D) ValueError

**3.** `ThrottlingException` should:

- A) Immediately jump to an unevaluated frontier model
- B) Back off and retry the same model
- C) Fail closed as if it were `AccessDeniedException`
- D) Disable IAM

**4.** `AccessDeniedException` should:

- A) Fall back to any model in the account
- B) Fail closed
- C) Be treated as throttle
- D) Trigger a fine-tune

**5.** The model id belongs in:

- A) Business-policy code scattered through the UI
- B) Gateway configuration, behind an eval gate
- C) The tool's JSON schema as a required field
- D) The vector index mapping

**6.** A tool schema change is:

- A) A cosmetic prompt edit
- B) A contract change for every model and caller
- C) Safe to do only in production
- D) Automatically versioned by the foundation model

**7.** The hardest lock-in to undo casually is usually:

- A) A temperature setting
- B) The embedding model behind an existing index
- C) A CloudWatch dashboard name
- D) The application font

**8.** Fine-tuning is the right first choice when:

- A) Facts change every hour
- B) You need stable behavior and have enough labels, while facts stay in retrieval or the prompt
- C) You have five example prompts and a deadline
- D) You want to avoid evaluation

**9.** Intelligent prompt routing is a weak fit when:

- A) You must know exactly which model produced a regulated answer
- B) You have a family of approved models and mixed difficulty
- C) Cost varies with prompt difficulty
- D) You log the model id that ran

**10.** A 200k context window means:

- A) You should paste the full corpus on every call
- B) You have a ceiling; the design still chooses prompt, long context, or RAG from cost, freshness, and tenancy
- C) Retrieval is impossible
- D) Output tokens are free

## Answers

1. B  2. B  3. B  4. B  5. B  6. B  7. B  8. B  9. A  10. B
