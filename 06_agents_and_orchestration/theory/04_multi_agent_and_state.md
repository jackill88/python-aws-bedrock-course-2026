# Multi-Agent Systems and State

Multi-agent collaboration (a supervisor model delegating to specialist agents) pays off when the specialists have different tools and different prompts, and you can afford the latency and the trace. It does not pay off as a way to avoid designing the workflow.

## When several agents are justified

| Signal | Prefer |
|--------|--------|
| One knowledge base, a handful of read tools | One agent, or Converse plus tools |
| Distinct authority (billing vs clinical vs identity) | Separate agents or, better, separate workflows with a supervisor that cannot hold every tool |
| The specialists would share one oversized tool list | Do not. Tool lists that long degrade selection and widen blast radius |
| You cannot explain a trace to an auditor | You are not ready to add agents |

A supervisor that can call every specialist, and a specialist that can call the supervisor, is a cycle with a token meter. Cap depth at one delegation unless you have a measured reason.

## State

| State | Lives | Dies |
|-------|-------|------|
| Turn | In the messages you just sent | End of the request |
| Session | Bedrock agent memory or your store, scoped to the user and tenant | Session timeout, explicit clear |
| Durable business state | The system of record the tool writes | When that system says so |

Do not store the system of record in the transcript. The transcript is a view. If the user says "actually refund 200" and the model agrees, nothing has happened until the tool commits.

Session memory is untrusted at read time: it can contain injection from an earlier turn, including from a document the user uploaded. Treat memory like a retrieved chunk.

## Trace

Every hop logs: request id, agent or workflow state, model id, tool name, approval id, input and output token counts. You do not need the full prompt in the hot log (Module 08). You do need enough to reconstruct which agent asked for which tool.

Review line: **"One trace id crosses the supervisor, the specialist, and the workflow. Three log formats is how incidents go cold."**

## Cost

Two agents can more than double the tokens, because the supervisor restates context. Put a per-request token ceiling on the whole collaboration, not on each agent separately. A ceiling per agent is how the sum escapes the budget.
