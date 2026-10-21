# Routing, Fallback, and Pinning

Once a tier is chosen, production needs a **route**: what happens when the call fails, and who is allowed to change the target. Routing is a reliability feature. It is also a quality and compliance feature, because the fallback model is a different product.

## Error to action

`fallback_route` maps a Bedrock error name to one action:

| Error | Action | Why |
|-------|--------|-----|
| `ThrottlingException` | `same_model_backoff` | Capacity, not a broken model. Retry with jitter on the same id (Module 03). Switching models just moves the stampede |
| `ModelTimeoutException`, `ModelErrorException`, `InternalServerException` | `fallback_model` | The attempt failed for a reason a different model or region might survive |
| `ValidationException`, `AccessDeniedException` | `fail_closed` | Retrying will not make a bad request or a missing permission valid. Do not fall back into a model the policy did not approve |
| `ServiceQuotaExceededException` | `same_model_backoff` | A quota is a ceiling on that model, not a cue to leak traffic onto an unreviewed one |

Any other error raises `ValueError` so unknown failures stay visible. Do not treat an unknown error as "retry forever."

Review line: **"Fallback is an explicit model you have evaluated, not whatever happens to be next on the price list."**

## Pinning vs routing

| Strategy | When | Risk |
|----------|------|------|
| **Pin a model id** | Regulated answers, evals that must match production, audits | You own deprecation and quota |
| **Inference profile (cross-region)** | Resilience inside a model family, regions you already approved | Data may be processed in profile destinations |
| **Intelligent prompt routing** | Mixed easy/hard prompts where cost matters and the family is approved | The model that answered is less predictable; eval both ends |
| **App-level tier map** | Different tasks (classify vs answer) | More moving parts, clearer cost |

For a regulated answer path, pin the id and keep fallback inside a **pre-approved pair**. For an internal classifier, a small tier with no fallback is often healthier than a clever router.

## Fallback design rules

1. The fallback model is in the threat model, the eval set, and the allow-list.
2. It has its own quota. Test it.
3. Tool schemas must validate on both models. A fallback that "mostly" emits JSON will break the workflow at the worst time.
4. Tell the audit log which model id actually ran.
5. Do not chain fallbacks more than once on a user request. Two hops is an incident; three hops is a cost bug.

## Quotas and profiles

A cross-region profile fails over **geography** for a model configuration. It is not permission to jump from a small model to a frontier model. Keep those as separate decisions: **where** it runs, and **which** model class runs.
