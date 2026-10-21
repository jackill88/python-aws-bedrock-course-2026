# System Design Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** Regulatory isolation maps to:

- A) `shared_index_metadata_filter`
- B) `account_per_tenant`
- C) `index_per_tenant`
- D) A shared account if the tenant count is high

**2.** Strong isolation maps to:

- A) `index_per_tenant`
- B) `account_per_tenant` always
- C) No filter
- D) `logical`

**3.** A high tenant count under regulatory isolation:

- A) Downgrades to a shared index
- B) Stays `account_per_tenant`
- C) Removes the need for IAM
- D) Forces batch inference

**4.** For a 1,000 ms RAG budget, retrieval receives:

- A) 150 ms
- B) 350 ms
- C) 100 ms
- D) 1,000 ms

**5.** The integer remainder of the latency split is added to:

- A) `guardrails`
- B) `model_ttft`
- C) `rerank`
- D) It is discarded

**6.** A budget under 100 ms:

- A) Is the interactive default
- B) Raises `ValueError` for this RAG split
- C) All goes to retrieval
- D) Selects batch

**7.** HR policy Q&A maps to:

- A) `managed_kb_rag`
- B) `workflow_human_approval`
- C) `hybrid_agent_read_default`
- D) `shared_platform_per_app_guardrails`

**8.** Claims adjudication maps to:

- A) An open agent with the system-of-record role
- B) `workflow_human_approval`
- C) `managed_kb_rag` with no human
- D) Prompt only

**9.** IT remediation maps to:

- A) `hybrid_agent_read_default`
- B) A pure agent with the production admin role
- C) `account_per_tenant` as the orchestration pattern
- D) Batch inference

**10.** A shared platform gives product teams:

- A) A long-lived key for every foundation model
- B) A gateway use-case name, with per-app guardrails that can be stricter than the baseline
- C) AdministratorAccess so agents are useful
- D) Production prompts in the sandbox by default

## Answers

1. B  2. A  3. B  4. A  5. B  6. B  7. A  8. B  9. A  10. B
