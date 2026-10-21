# Prompts as Artifacts

Bedrock prompt management exists so a prompt can have an identifier, a version, and a variant. Use it, or use the same discipline in your own store. The failure mode is the same either way: an unreviewed edit changes production behavior with no diff and no rollback.

## What is in the artifact

| Piece | Changes when |
|-------|----------------|
| System instructions | Policy, tone, or tool rules change |
| Few-shot examples | You are correcting a repeated miss — and you have checked they are not sensitive data |
| Output contract | The downstream parser changes |
| Model parameters | Temperature, max tokens, stop sequences |
| Linked guardrail version | Safety policy changes |
| Eval set id | You need to know which bar this version cleared |

The user message, retrieved chunks, and tool results are **inputs**, not part of the artifact. Mixing them into the versioned prompt is how one tenant's document becomes the next tenant's instruction.

## Environments

| Environment | Prompt versions | Data |
|-------------|-----------------|------|
| Dev | Authors may draft | Synthetic or approved samples only |
| Staging | The candidate version | A frozen eval set, production-like schemas |
| Prod | Only a promoted version | Real traffic |

Hot-editing the production prompt in the console is an incident technique with a ticket, not a delivery process. Roll forward by publishing a version; roll back by pinning the previous version. The gateway reads the pin.

Review line: **"If we cannot diff it and roll it back, it is not a prompt system. It is a shared scratchpad."**

## Parameters travel with the prompt

A prompt version that assumes temperature 0 and a sibling config at temperature 1 is two systems. Store inference parameters beside the text. Module 02 put the model id in config; the prompt version may **declare the tier it was evaluated against**. Promoting a prompt onto a different tier without re-running the gate is a new release, even if the words did not change.

## Ownership

| Role | Owns |
|------|------|
| Product + subject matter | What the assistant is allowed to claim |
| Platform | The store, the gateway pin, the rollback |
| Security | The injection suite and the guardrail link |
| The on-call | Which version is live, visible on the dashboard |

No single hero "prompt engineer" is the control. The artifact has the same change management as a policy-bearing config file, because that is what it is.
