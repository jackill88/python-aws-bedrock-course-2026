# Platform Mental Model

Amazon Bedrock is a **managed inference platform**, not a chatbot product and not a place you train a base model from scratch. A lead architect draws the box as an API boundary in front of foundation models from several providers, plus first-party capabilities around that API: knowledge bases, agents, guardrails, evaluation, and customization.

The system you are accountable for sits **around** that boundary: identity, data, prompts, tools, evaluation, cost, and the user journey.

## What you are actually buying

| Capability | What it is | What it is not |
|------------|------------|----------------|
| Foundation-model inference | Hosted models invoked by API | A guarantee of answer quality |
| Choice of providers | Claude, Llama, Nova, Mistral, embeddings, rerankers, and others, varying by region | Freedom from provider terms |
| Orchestration features | Knowledge Bases, Agents, Flows, Guardrails | A substitute for your domain workflow |
| Operational controls | IAM, private network, KMS, invocation logging, quotas | Automatic compliance |

Review line: **"Bedrock hosts the model call. We still own the product behavior."**

## Three adjacent options

When someone says "just use Bedrock," force the placement decision.

| Option | Choose it when | You still operate |
|--------|----------------|-------------------|
| **Bedrock** | You want managed multi-model inference, AWS identity, and a short path to RAG/guardrails | Prompts, evals, tools, data access, product UX |
| **SageMaker** | You need custom training loops, your own container, or a model Bedrock does not host the way you require | Cluster, images, scaling, much of the inference stack |
| **Self-managed GPUs** (EC2, EKS, or outside AWS) | You have a hard residency, cost, or open-weight constraint Bedrock cannot meet | Drivers, serving stack, capacity, security patching |

Marketplace models inside Bedrock are a fourth case: the API looks similar, but **commercial terms and data handling can differ**. Call that out in the review, do not hide it under "it's still Bedrock."

## The architect's picture

```
Clients (app, batch job, agent runner)
    → Your gateway (authz, tenant, budget, audit id)
        → Guardrails / policy
        → Retrieval or tools (your data plane)
        → Bedrock runtime (Converse, InvokeModel, Retrieve)
            → Foundation model in a region or inference profile
        → Your post-checks (schema, grounding, citation)
    → User or downstream system
```

Every arrow needs an owner, a timeout, and a failure story. "The model will figure it out" is not a failure story.

## Questions to ask in the first review

| Question | Why it changes the design |
|----------|---------------------------|
| Interactive or asynchronous? | On-demand vs batch, streaming vs job |
| Which regions may process the prompt? | Inference profiles can leave the source region |
| Is the corpus larger than the context window, and does it change? | RAG vs prompt stuffing vs fine-tune |
| Can a tool move money, data, or production state? | Workflow and human approval, not an open agent loop |
| What does "good" mean in numbers? | Quality SLOs, not only HTTP 200 |
| Who pays, and what is the ceiling? | Token budgets, per-tenant limits, provisioned commit |

## What a weak design looks like

- One model id hard-coded in twelve services, with no fallback and no deprecation owner
- Retrieved documents concatenated into the prompt with no tenant filter
- Retries wrapped around a tool that charges a customer
- Success defined as `stopReason == end_turn`
- Cost forecast copied from a single demo prompt

## What you should be able to say

"We pin the use case to a **model class** behind a gateway, call **Converse** for generation, keep embeddings on **InvokeModel**, log **metadata** everywhere and **raw prompts** only in a restricted store, and we size **on-demand vs provisioned vs batch** from latency and predictability — not from the tutorial we saw first."
