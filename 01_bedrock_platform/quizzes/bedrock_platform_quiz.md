# Bedrock Platform Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** A lead architect's default description of Amazon Bedrock is:

- A) A chatbot your users log into
- B) A managed inference platform in front of foundation models, with your system built around the API
- C) A GPU cluster you patch yourself
- D) A data warehouse for prompts

**2.** Which call is data-plane?

- A) `CreateGuardrail`
- B) `PutModelInvocationLoggingConfiguration`
- C) `Converse`
- D) `ListFoundationModels`

**3.** Prompt and completion bodies are:

- A) Always present in CloudTrail management events
- B) Available when you explicitly enable model invocation logging, which you then treat as sensitive
- C) Impossible to retain under any AWS feature
- D) Stored only inside the foundation-model weights

**4.** Cross-region inference profiles matter in a residency review because:

- A) They never leave the caller's region
- B) Destination regions on the profile may process the prompt
- C) They disable IAM
- D) They force batch inference

**5.** Choose batch inference when:

- A) A user is waiting on a 2-second SLO
- B) The job is asynchronous and not latency-sensitive
- C) You need the lowest idle bill and the lowest latency at once
- D) The model has no on-demand quota

**6.** Provisioned throughput is the right commercial shape when:

- A) Traffic is a handful of prototype calls
- B) You want zero cost at idle, above all else
- C) Latency-sensitive traffic has a predictable, high baseline that justifies a commit
- D) The work can wait overnight

**7.** Below a high, steady baseline, this course prefers on-demand over provisioned because:

- A) On-demand has no quotas
- B) A provisioned commit can cost more than the tokens at low volume
- C) Batch is illegal under 100,000 requests
- D) IAM cannot restrict provisioned models

**8.** "Bedrock does not train base models on customer prompts" means:

- A) You no longer need IAM
- B) Marketplace models need no terms review
- C) That specific commitment is AWS's; who may invoke, and what prompts are allowed, remains yours
- D) Invocation logs are public

**9.** Adopting an interface VPC endpoint for the runtime is:

- A) Automatic for every account
- B) The customer's design choice: create it, route to it, and restrict the public path
- C) A property of the foundation-model weights
- D) Only relevant to S3

**10.** A production application role should typically be allowed to:

- A) `Converse` and `Retrieve`, not rewrite account logging configuration
- B) Create provisioned throughput from the request path
- C) Disable CloudTrail when latency is high
- D) Share its keys with the sandbox account

## Answers

1. B  2. C  3. B  4. B  5. B  6. C  7. B  8. C  9. B  10. A
