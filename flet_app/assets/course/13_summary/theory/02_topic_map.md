# Topic Map

```
Placement and money          01 platform, 09 capacity and cost
Model identity               02 tiers, pins, fallback, lifecycle
The call                     03 Converse, budgets, cache, retries
Instructions                 04 artifacts, trust zones, promotion
Knowledge                    05 grounding, chunks, filters, citations
Action                       06 workflows, tools, approval, traces
Harm and claims              07 guardrails, PII, grounding
Trust in the platform        08 IAM, network, logs, residency, accounts
Whether it is actually up    09 SLOs including quality
Whether a change may ship    10 metrics, judges, release gate
The review itself            11 cases, tenancy, latency budget
Where the caller runs          12 Lambda, ECS/Fargate, edge timeouts
```

## How the pieces meet on one request

```
User
  → gateway on Lambda or ECS (IAM use-case, tenant, budget, edge timeout, trace id)
      → retrieve with the filter
      → fit the token budget
      → guardrail input
      → Converse (pinned model, pinned prompt, cache on the stable prefix)
      → guardrail output + grounding
      → cite or abstain
      → if a write was proposed: workflow, idempotency key, approval
  → metrics: latency slices, tokens, groundedness, stop reason
```

A failure at any arrow has a module: throttle (03, 09), empty retrieval (05), injection in a chunk (04, 07), cross-tenant passage (05, 08), double charge (06), surprise region (08), pretty and ungrounded text (07, 10).

## Practice order if you are short on time

| If you only have a day | Do |
|------------------------|----|
| You already know the API | Modules 05, 06, 08, 11, and their tests |
| You are new to Bedrock | Modules 01 through 04, then 11's case studies |
| You own an existing bot that "mostly works" | 07, 09, 10 — safety, SLOs, and the release gate |
| You are choosing Lambda or ECS | Module 12, then the timeout and retry challenges |

Then implement the stubs. Reading the decision tables is not the same as being able to reproduce them under a test.
