# Defense in Depth

Guardrails reduce harm on the text path. Authorization, tenancy, and tool approval do not move into the guardrail because a filter cannot be your IAM policy.

## Layers that stack

| Layer | Stops |
|-------|--------|
| IAM and the gateway allow-list | Calls to models, knowledge bases, and guardrail versions you did not approve |
| Tenant filter on retrieval | Cross-tenant passages |
| Trust zones and the injection suite | Instructions hidden in documents and tool results |
| `ApplyGuardrail` on tool arguments | A subset of dangerous or sensitive arguments before execution |
| Tool implementation | The actual authorization, idempotency, and approval |
| Output guardrail and grounding | User-visible harm and ungrounded claims |
| Eval gate | A release that regresses any of the above |

If you remove any row, name the risk you accepted. "The guardrail covers it" is not a name.

## Prompt injection, again

A denied topic will catch some jailbreaks and miss others. Assume the model can be nudged. The durable controls are: tools do not trust arguments that widen scope, retrieval is filtered outside the model, and the output cannot trigger a side effect by itself. An injection suite that only attacks the system prompt, and never the retrieved chunk, is testing the wrong door.

## User experience of a block

| Intervention | User should get |
|--------------|-----------------|
| Denied topic | A short refusal in your voice, plus a path to a human if the topic is adjacent to real work |
| PII mask | The answer, with the mask. Do not also apologize in a way that reveals the value |
| PII block | No answer, and no echo of the identifier |
| Grounding fail | Abstain. Do not show the draft "for transparency" in a regulated UI |

Log the intervention type for the product owner. A spike in denies is either an attack or a guardrail that no longer matches the task. Both are reviews. Neither is fixed by disabling the guardrail on Friday.

Review line: **"Disabling the guardrail is a change request with an expiry, not an incident mitigation you forget to undo."**

## Batch and async

The same policies apply to batch inference and to agents. An agent that calls tools has already left the text filter unless you check arguments. A batch job that writes summaries into a system customers read is user-facing output even though the original caller was a scheduler.
