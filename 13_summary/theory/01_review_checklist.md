# Review Checklist

Use this on a real design. A row you cannot answer is the next module to revisit.

| # | Question | Module |
|---|----------|--------|
| 1 | Is this Bedrock, SageMaker, or self-hosted, and why? | 01 |
| 2 | Which calls are control-plane, and which role holds them? | 01, 08 |
| 3 | On-demand, provisioned, or batch — from latency and predictability, not from habit? | 01, 09 |
| 4 | What tier, what pinned id, what measured fallback? | 02, 09 |
| 5 | What is config, what is a versioned prompt, what is a tool contract? | 02, 04 |
| 6 | Converse for generation, InvokeModel only where the unified API does not fit? | 03 |
| 7 | Token budget: output reserved, system intact, retrieval dropped before history? | 03 |
| 8 | Retry only when the call is safe to repeat? | 03, 06 |
| 9 | Prompt version, injection suite, human promotion? | 04 |
| 10 | Grounding choice: prompt, long context, RAG, fine-tune, or both? | 05 |
| 11 | Chunk strategy and maximum age of a citable chunk? | 05 |
| 12 | Tenant filter in a gateway the model cannot skip? Isolation class named? | 05, 11 |
| 13 | Cite or abstain on the user-facing path? | 05, 07 |
| 14 | Workflow versus agent versus hybrid, from tool risk? | 06 |
| 15 | Idempotency keys minted by the gateway on writes? | 06 |
| 16 | Human approval binding arguments, not a sentence in the chat? | 06 |
| 17 | Guardrail version pinned, stages matching the surface, PII actions by audience? | 07 |
| 18 | Grounding failure abstains? | 07 |
| 19 | Runtime role fits on one screen, model ARNs named? | 08 |
| 20 | Restricted data on an interface endpoint, public path closed? | 08 |
| 21 | Hot logs without raw prompts; secrets dropped? | 08 |
| 22 | Every processing region, including profile destinations, on the allowed list? | 08 |
| 23 | SLOs for availability, groundedness, and latency, with separate breach actions? | 09 |
| 24 | Cost showback by use case, cache tokens not double-counted? | 09 |
| 25 | Recall and groundedness both reported? Judge method matches the claim? | 10 |
| 26 | Safety, shadow regression, and unjustified cost jumps block the release? | 10 |
| 27 | Latency budget sums to the user promise? | 11 |
| 28 | This case matches a known pattern, or it got its own review? | 11 |
| 29 | Does this caller fit Lambda, including the edge timeout, or does it need ECS/Fargate? | 12 |
| 30 | If Lambda is invoked asynchronously, what stops a retry from repeating a model call or a write? | 12 |

Review line: **"Thirty rows. The design is ready when each one has an owner and a number or a named pattern."**
