# Lifecycle and Lock-in

Models are deprecated, fine-tunes are tied to a base, and prompts encode assumptions about a tokenizer and a tool format. Lock-in is not "we used AWS." Lock-in is **how many weeks to change the model id without a user-visible regression**.

## What actually couples you

| Coupling | How tight | How you loosen it |
|----------|-----------|-------------------|
| Model id scattered in code | Tight | One gateway config per use case |
| Prompt tuned to one model's quirks | Medium | Versioned prompts, eval gate on model change (Module 04, Module 10) |
| Tool schema | Medium | JSON schema owned by the tool, not by the prompt author |
| Fine-tune or continued pre-train | Tight | Treat custom weights as a product with a rebuild plan |
| Knowledge-base embeddings | Tight | Record the embedding model id; re-embed is a migration project |
| Provisioned throughput on one model | Commercial | Commit length matches how long you intend to stay |

Review line: **"Embeddings lock in harder than chat prompts. A model swap that does not re-embed is a retrieval bug."**

## Lifecycle states

| State | Architect action |
|-------|------------------|
| Candidate | Offline eval only, no production data unless the sandbox policy allows it |
| Approved | On the allow-list, IAM can invoke it, runbooks name it |
| Default | The config mapping for a use case |
| Fallback | Evaluated, quota reserved or at least known, not a surprise |
| Deprecated | Dated exit: new traffic stops, in-flight fine-tunes rebuilt, dashboards still distinguish it |
| Retired | IAM deny, config removed |

Someone owns the calendar. "We'll notice when it breaks" means you notice in production.

## Customization is a product decision

Fine-tuning and continued pre-training exist for **some** Bedrock models, not as a universal knob.

| Need | Prefer |
|------|--------|
| New or changing facts | RAG, not a fine-tune |
| Stable style, format, or policy tone, with enough labels | Fine-tune, and still retrieve facts |
| Domain language the tokenizer barely represents | Continued pre-train only with a clear corpus and eval, rarely the first move |
| One team wants a custom model "for quality" | Demand the eval delta versus a better prompt and a stronger tier |

Custom models have a hosting and IAM story of their own (provisioned throughput is often required to invoke them). Do not assume a custom model is a drop-in on-demand id.

## Abstraction boundary

`abstraction_boundary` tells you where a change is allowed to live:

| Component | Boundary | Meaning |
|-----------|----------|---------|
| `model_id` | `config` | Change without an application release, behind the eval gate |
| `prompt_template` | `versioned_artifact` | Reviewed, versioned, promoted. Not a string in a Lambda edited live |
| `tool_schema` | `contract` | A breaking change is an API change for every model and every caller |
| `business_policy` | `application` | Refund rules, entitlements, and who may approve do not belong inside the model |

Unknown components raise `ValueError`.

## Exit test

You are not locked in beyond recovery if you can answer yes:

- Can we point the use case at the fallback id with a config change?
- Do we have an eval set that must pass before that change?
- If embeddings change, is re-index scheduled as part of the same change?
- Can IAM deny the old id on a known date?
