# Observability and Incidents

CloudWatch metrics on the runtime (invocations, latency, throttles, client and server errors, token counts) tell you the API is unhappy. They do not tell you the answer got worse. You add product metrics.

## Minimum dashboard

| Panel | Source |
|-------|--------|
| Invocations, throttles, server errors | Runtime metrics, split by model id |
| p50 / p95 latency | Gateway, split into retrieval, guardrail, model time-to-first-token, completion |
| Token counts and cache hit rate | Usage fields, by use case |
| Groundedness and guardrail interventions | Your trace, by policy type |
| Abstain rate | Citation policy outcomes |
| Tool errors and approval waits | Workflow, not the model metric |

One trace id connects them (Module 06). Logs follow the field policy (Module 08): hot logs stay small; raw prompts stay in the restricted store.

## First questions in an incident

| Symptom | Look at |
|---------|---------|
| Sudden throttles | Quota, a new tenant, a retry storm, a load test left on |
| Latency up, throttles flat | Retrieval or a larger prompt, not the model quota |
| Errors up, one model only | That model's health and your fallback route |
| Quality down, API green | A prompt pin, a bad sync, an embedding mismatch, a guardrail version |
| Cost up, traffic flat | Output length, a cache miss, an agent hop cap that moved |

Rollback is a config pin: previous prompt version, previous model id, previous guardrail version. If rollback needs a deploy, you do not have a pin.

Review line: **"The first mitigation is the previous known-good pin, not a new prompt written on the call."**

## Game day

Once before launch, and after any topology change:

1. Deny the primary model in a test role and confirm fallback stays inside the allow-list.
2. Empty the knowledge base for one tenant and confirm abstain, not a hallucinated policy.
3. Trip the tenant budget and confirm shed, not a shared outage.
4. Confirm an on-call who is not the author can find the live prompt version from the dashboard alone.
