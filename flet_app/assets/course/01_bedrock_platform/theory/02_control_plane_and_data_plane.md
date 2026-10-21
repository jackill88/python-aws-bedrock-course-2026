# Control Plane and Data Plane

Bedrock has two speeds of API, and they fail differently. Mixing them up produces the wrong IAM policy, the wrong log, and the wrong incident channel.

## Definitions

| Plane | Examples | Characteristics |
|-------|----------|-----------------|
| **Control** | Create or update a guardrail, knowledge base, agent, prompt, provisioned throughput; put invocation-logging configuration; list foundation models | Fewer calls, IAM-admin sensitive, changes live configuration, shows up as management activity |
| **Data** | `Converse`, `ConverseStream`, `InvokeModel`, `Retrieve`, `RetrieveAndGenerate`, `ApplyGuardrail` | High volume, on the user path or the batch path, carries prompt and document content |

Review line: **"CloudTrail is not a transcript of what the model said."** Management calls are audited as control-plane activity. Prompt and completion bodies are **not** in those trails. If you need the content, you enable **model invocation logging** (and you treat that store as sensitive).

## Why the split matters

| Decision | Control plane | Data plane |
|----------|---------------|------------|
| Who can do it | Platform team, often via pipeline | Application runtime role |
| Blast radius | A bad guardrail version affects every caller | A bad prompt affects one request — until you ship it to everyone |
| Latency budget | Seconds to minutes is normal | Tens to thousands of milliseconds, on the SLO |
| Network path | AWS APIs from a deploy role | Runtime VPC endpoint (`bedrock-runtime`, and agent/KB runtime if you use them) |
| Data classification | Configuration, ARNs, versions | Customer text, documents, tool results |

Give production runtimes **invoke and retrieve**, not **create knowledge base** or **put logging configuration**. Platform automation holds the control-plane role. Humans do not share that role with the app.

## Runtime surfaces you will actually choose

| API | Use |
|-----|-----|
| `Converse` / `ConverseStream` | Chat and generation across models that support the unified schema: messages, system, tools, guardrail config |
| `InvokeModel` | Embeddings, image models, and payloads that do not fit Converse |
| `Retrieve` | Your code owns the prompt. Preferred when you must control citations, eval, and tenant filters |
| `RetrieveAndGenerate` | Managed retrieve-then-answer. Faster to demo, less control |
| `ApplyGuardrail` | Policy check **without** a model call. Use it on tool arguments and on untrusted text before it reaches a tool |

Agents and Flows are products on top of these calls. They are not a third plane; they are control-plane resources that perform data-plane calls on your behalf. Their execution role is a privileged runtime identity. Review it like one.

## Region is part of the data plane

A model is enabled and invoked **in a region**, or through an **inference profile** that may route to other regions. Cross-region inference improves resilience and can change **where the prompt is processed**.

For a residency review, list:

1. The region of the caller
2. Every destination region on the inference profile
3. Where invocation logs, knowledge-base indexes, and embeddings are stored

"We called `us-east-1`" is incomplete if the profile's destinations include other regions.

## Failure domains

| Failure | Plane | First response |
|---------|-------|----------------|
| Throttling, model timeout | Data | Backoff, fallback model, shed load. Do not "fix" it by granting more admin IAM |
| Access denied on `InvokeModel` | Data | Resource ARN, inference profile, or missing model access — runtime policy |
| Cannot update a guardrail | Control | Pipeline role, not the task role |
| Logs missing prompt text | Control config | Invocation logging was never enabled, or content logging was left off on purpose |

## Mapping to the challenge

`classify_api_plane` returns `"control"` or `"data"`.

| API | Plane |
|-----|-------|
| `CreateGuardrail`, `CreateKnowledgeBase`, `PutModelInvocationLoggingConfiguration`, `CreateProvisionedModelThroughput`, `ListFoundationModels` | control |
| `Converse`, `ConverseStream`, `InvokeModel`, `Retrieve`, `RetrieveAndGenerate`, `ApplyGuardrail` | data |

Unknown names raise `ValueError`. Listing models is control-plane metadata, even though it is read-only. `ApplyGuardrail` carries content, so it is data-plane.
