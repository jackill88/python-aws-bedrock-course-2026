# Callers, Not Hosts

Lambda and ECS do not run the foundation model. Bedrock does. The compute you choose is the process that calls `Converse`, `Retrieve`, `ApplyGuardrail`, or a tool the agent asked for. A review that puts GPU instances in ECS "for the model" has mixed up the host with the caller.

Review line: **"Bedrock is the inference fleet. Lambda or Fargate is only the client."**

## What each one is for

| Runtime | It is good at | It is a poor fit for |
|---------|---------------|----------------------|
| **Lambda** | A stateless invocation: API turn, S3 or EventBridge event, SQS message that finishes in time, Bedrock Agent action group | A WebSocket you must hold, a job that can pass 15 minutes, a process you expect to stay warm as a pool of long-lived SDK clients |
| **ECS on Fargate** | A service that holds connections, a worker whose single item can outlive Lambda, a gateway with a min task count | Scale-to-zero for a rarely used internal tool. You pay for the tasks you leave running |
| **ECS on EC2** | A caller that truly needs a host you manage | Ordinary Bedrock gateways. You are not serving the model, so you do not need GPUs on this tier |

Fargate is the default in this course. Say EC2 only when Fargate cannot do the thing, and that reason is almost never "the LLM."

## The pattern

`choose_compute(pattern, max_duration_s)` returns `lambda` or `ecs_fargate`.

| Input | Meaning |
|-------|---------|
| `event` | One stateless invocation. Nothing about this call requires the same process to still be there afterward |
| `response_stream` | Tokens streamed on the response of this one invocation (Lambda response streaming or a single ECS request) |
| `held_session` | This process must hold the client connection or the agent session across time: WebSocket, sticky in-memory session |
| `max_duration_s` | Worst case for that unit of work, in seconds. Negative is `ValueError`. Unknown pattern is `ValueError` |

| Order | Result |
|-------|--------|
| `held_session` | `ecs_fargate`, even if one turn is short. The connection outlives a single invoke |
| `max_duration_s > 900` | `ecs_fargate`. One Lambda invocation cannot be configured past 900 seconds |
| Otherwise (`event` or `response_stream`, at most 900 seconds) | `lambda` |

```python
def choose_compute(pattern: str, max_duration_s: int) -> str:
    if pattern not in {"event", "response_stream", "held_session"} or max_duration_s < 0:
        raise ValueError("bad pattern or duration")
    if pattern == "held_session" or max_duration_s > 900:
        return "ecs_fargate"
    return "lambda"
```

900 seconds is included in Lambda. 901 is not. A short token stream is still Lambda. "We might stream" is not by itself a reason to run a cluster.

## What this does not decide

Module 01 still chooses on-demand, provisioned throughput, or batch. Module 06 still chooses workflow versus agent. A Fargate service can call batch for a backfill and Converse for a chat. A Lambda can be the action group in front of a Step Functions approval. Compute is the process boundary, not the product architecture.
