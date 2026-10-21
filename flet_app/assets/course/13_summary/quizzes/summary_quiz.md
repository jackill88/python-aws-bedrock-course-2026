# Summary Quiz

10 multiple-choice questions. Answers are at the bottom. These check whether the modules stayed connected.

---

**1.** The runtime role should be able to:

- A) Change the account's logging configuration during a request
- B) Invoke the pinned production model and retrieve only the knowledge bases it serves
- C) Subscribe to Marketplace models
- D) Read every tenant's raw prompts in the hot log

**2.** A user-facing policy answer with no retrieved passage should:

- A) Use the model's memory and skip the citation
- B) Abstain or disclose that it is ungrounded
- C) Switch to a frontier model and try again in a loop
- D) Count as a healthy availability success with no separate metric

**3.** An irreversible tool belongs in:

- A) The open agent loop by default
- B) A workflow with human approval
- C) The system prompt
- D) The embedding model

**4.** Prompt text in the application log group should be:

- A) Kept for convenience
- B) Kept out of the hot log; raw text only in a restricted store if you need it at all
- C) Placed in the cache prefix for all tenants
- D) Sent to the sandbox account

**5.** `ThrottlingException` on an idempotent read should:

- A) Fail closed as access denied
- B) Back off on the same model, within the attempt cap
- C) Immediately call an unapproved model
- D) Disable the guardrail

**6.** Fine-tuning is the wrong sole answer when:

- A) The tone is stable and the facts change every hour
- B) You have a small static style guide and hundreds of labeled examples
- C) You also retrieve the changing facts
- D) The prompt is versioned

**7.** A shadow quality drop of more than two points should:

- A) Ship if the demo looked better
- B) Block the release
- C) Be averaged into a thumbs-down metric later
- D) Raise temperature

**8.** Cross-region inference means the residency review must list:

- A) Only the region in the SDK call
- B) The caller region and every profile destination, plus where logs and the index live
- C) Only the CloudTrail home region
- D) No regions, because Bedrock is global by default for data

**9.** The latency slices for the RAG budget must:

- A) Sum to the user-visible budget
- B) Each equal the whole budget
- C) Ignore guardrails
- D) Be chosen by the model at runtime

**10.** The platform gives product teams:

- A) A use-case on the gateway
- B) `bedrock:*` so they are not blocked
- C) Production data in the sandbox
- D) Permission to hot-edit the shared guardrail draft

## Answers

1. B  2. B  3. B  4. B  5. B  6. A  7. B  8. B  9. A  10. A
