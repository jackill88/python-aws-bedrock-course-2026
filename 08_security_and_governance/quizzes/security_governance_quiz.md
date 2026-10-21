# Security Governance Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** `app_runtime` may:

- A) Invoke production and retrieve from the knowledge base
- B) Read invocation logs and create guardrails
- C) Manage provisioned throughput
- D) Invoke dev only

**2.** `product_dev` may:

- A) `invoke_prod`
- B) `invoke_dev`
- C) `read_invocation_logs`
- D) `retrieve_kb` in production

**3.** `data_scientist` may read invocation logs and:

- A) Invoke production
- B) Invoke dev, not production
- C) Create guardrails
- D) Buy provisioned throughput

**4.** An allow on every foundation-model ARN is:

- A) Least privilege, because the action is specific
- B) The same class of mistake as `bedrock:*`, one level down
- C) Required for guardrails
- D) A VPC endpoint

**5.** Restricted data from a VPC should use:

- A) The public runtime endpoint, because of TLS
- B) An interface VPC endpoint, with the public path closed
- C) A NAT gateway only, with no endpoint policy
- D) The S3 website endpoint

**6.** Prompt text in logs should be:

- A) `keep` in the application log group
- B) `redact_or_separate_restricted_store`
- C) `drop` always, with no option for a restricted audit store
- D) Copied into the system prompt

**7.** `authorization` headers are:

- A) `keep`
- B) `drop`
- C) `redact_or_separate_restricted_store`
- D) Hashed into the request id

**8.** An empty list of processing regions is:

- A) Allowed, because nothing left the account
- B) Not allowed
- C) Allowed for public data only
- D) A control-plane success

**9.** Cross-region inference profiles affect residency because:

- A) They ignore destination regions
- B) Destinations must be included in the processing-region list
- C) They disable KMS
- D) They force `bedrock:*`

**10.** Marketplace model subscription in production is:

- A) A normal developer click
- B) A governance event: terms, data handling, and usually an SCP backstop
- C) Covered automatically by "Bedrock does not train on prompts"
- D) Required for every RAG design

## Answers

1. A  2. B  3. B  4. B  5. B  6. B  7. B  8. B  9. B  10. B
