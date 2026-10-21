# The Converse Contract

Bedrock exposes model-specific payloads through `InvokeModel` and a unified messages API through `Converse` and `ConverseStream`. A platform with more than one model standardizes **generation** on Converse. You keep InvokeModel for embeddings, image-only models, and the few parameters Converse cannot express (`additionalModelRequestFields` covers many of the rest).

Review line: **"One request shape for generation. Model-specific payloads stay at the edge."**

## What belongs in the request

| Field | Role |
|-------|------|
| `modelId` | A pinned id or an inference-profile id. This is config, not a prompt |
| `system` | Stable instructions. Cache candidate. Not a place for end-user text |
| `messages` | User and assistant turns, plus tool results. Untrusted |
| `inferenceConfig` | `maxTokens`, `temperature`, `topP`, stop sequences |
| `toolConfig` | Tool schemas and `toolChoice`. A contract (Module 02) |
| `guardrailConfig` | Identifier, version, and whether to return the trace |

```python
response = client.converse(
    modelId=model_id,
    system=[{"text": system_text}],
    messages=[{"role": "user", "content": [{"text": user_text}]}],
    inferenceConfig={"maxTokens": 800, "temperature": 0.2},
    guardrailConfig={
        "guardrailIdentifier": guardrail_id,
        "guardrailVersion": guardrail_version,
        "trace": "enabled",
    },
)
```

The snippet is illustrative. Production code goes through your gateway so the model id, guardrail version, and max tokens are not chosen by the caller ad hoc.

## Response fields architects actually use

| Field | Use |
|-------|-----|
| Output message | The user-visible text or the tool use blocks |
| `stopReason` | `end_turn`, `tool_use`, `max_tokens`, `guardrail_intervened`, and others. `max_tokens` is a truncated answer, not a success |
| Usage | Input, output, and cache token counts for cost and budgets |
| Trace | Guardrail assessments, when you asked for them |

Treat `guardrail_intervened` as a product path: a refusal or a masked completion, with a user-facing message you wrote, not the raw block payload dumped to the client.

## Gateway responsibilities

The application should not call `bedrock-runtime` from a dozen services with copied clients. One gateway:

1. Authenticates the caller and stamps a tenant and a request id
2. Resolves use case → model id, guardrail version, max tokens
3. Enforces the token budget before the call
4. Emits metrics: model id, stop reason, latency, token counts, tenant
5. Is the only principal allowed to `bedrock:InvokeModel` / `bedrock:Converse` in production

Direct SDK calls from notebooks against production roles are an exception process, not a pattern.

## Idempotency of the call itself

A pure generation call is safe to retry from the model's point of view: you may pay twice and get different text if temperature is above zero. It is **not** safe to retry if the model already asked for a non-idempotent tool and you executed it. The retry decision in this module takes an explicit `idempotent` flag for that reason.
