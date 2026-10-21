# Streaming, Timeouts, and Partial Failure

Interactive experiences should stream. Batch jobs should not. The failure mode of a stream is a **partial answer**: the user has seen tokens, your logs have an incomplete message, and a blind retry duplicates the visible reply.

## When to stream

| Caller | API | Timeout that matters |
|--------|-----|----------------------|
| UI chat | `ConverseStream` | Time to first token, and a stall timeout between deltas |
| Service that needs the full JSON | `Converse` | End-to-end deadline shorter than the caller's deadline |
| Overnight eval or backfill | Batch inference | Job-level deadline, not a socket timeout |

Streaming does not remove the need for `maxTokens`. It only changes when the user starts reading.

## Deadlines

Set three clocks, not one:

| Clock | Protects |
|-------|----------|
| Client deadline | The user or the upstream SLA. Cancel the work when this fires |
| Gateway deadline | Slightly shorter than the client, so you can return a controlled error |
| Model / read timeout | A stalled stream. A connection that drips forever is not healthy |

Leave room for retrieval and guardrails **before** the model clock starts. A 3-second user budget with a 3-second model timeout and a 1-second search will always fail.

## Partial failure

| stop or error | What the user should experience |
|---------------|---------------------------------|
| `end_turn` | The answer, still subject to schema and grounding checks |
| `max_tokens` | A truncated answer. Do not present it as complete. Raise the cap only if the eval says the task needs it |
| `tool_use` | No final answer yet. Validate the tool call, then continue the loop or hand it to a workflow |
| `guardrail_intervened` | Your refusal or redaction copy |
| Stream dies mid-way | Stop. Do not automatically restart if the user already saw the partial text, unless the UI replaces it explicitly |
| Timeout before any token | Safe to retry **if** no tool with side effects has run |

Review line: **"A retry is a second answer. Decide whether the user, the bill, and the tools can absorb it."**

## Tool loops

Converse tool use is a loop you own: the model returns `toolUse` blocks, your code runs the tool, you send `toolResult` blocks back. Cap the number of hops (a small integer, often 3–8 depending on the task). A loop without a cap is an availability and cost incident.

If the tool can change production state, the loop does not sit inside an automatic retry. Module 06 makes that a workflow decision. This module only requires the retry function to **refuse** a non-idempotent transient retry.
