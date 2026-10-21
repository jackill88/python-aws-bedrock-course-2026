# ECS and Fargate

Choose Fargate when the unit of work holds a connection or can run past a single Lambda invocation. The task is still a Bedrock **client**. The model id, the guardrail version, and the token budget do not get more generous because the CPU is yours.

## Service shape

| Piece | Architect's default |
|-------|---------------------|
| Launch type | Fargate |
| Network | `awsvpc`, private subnets, interface endpoint for `bedrock-runtime` when the data class requires it |
| Identity | A task role with `Converse` / `InvokeModel` / `Retrieve` on the named ARNs. Not `bedrock:*`. Not the same role that deploys the service |
| Edge | ALB for HTTP and for streams, with the idle timeout raised to cover the longest honest stream. Default 60 seconds will cut a slow answer |
| Count | A minimum task count only when a cold start breaks the latency SLO. Otherwise let it scale, and still put a maximum on it |
| Health | The load-balancer check hits your process, not Bedrock. A model throttle must not mark the task unhealthy and drain the service |

`platform_timeout_s("ecs_task")` is `None` because AWS does not impose the 29-second or 900-second caps on the task itself. You still set a deadline. An unbounded HTTP handler in front of Converse is how one tenant holds a worker until the bill moves.

## What belongs here

| Workload | Why Fargate rather than Lambda |
|----------|--------------------------------|
| WebSocket or a session pinned in memory | `held_session` |
| A document or agent turn whose worst case is over 900 seconds | Lambda cannot be given that timeout |
| A steady pool of SDK clients against provisioned throughput | You want warm connections and a min count you can see |
| A parser-plus-model pipeline with a large working set and a long tail | The job is a worker, not a 29-second API integration |

A short, spiky, stateless call does not become a better design by landing on Fargate. You take on an image, a deploy, a cluster, and idle cost. Say that trade in the ADR.

## Deploys and drain

Rolling deploys must drain in-flight streams. A task that calls Bedrock and is killed at SIGTERM mid-tool-write is the same class of problem as a Lambda timeout: you may not know whether the tool landed. Cap the tool call, pass the idempotency key, and on SIGTERM stop accepting new work and finish or explicitly abandon the in-flight turn. The circuit breaker on the ECS deployment is what stops a bad image from taking every task.

Review line: **"The task role is the runtime role from Module 08. The cluster admin role is not."**

Logs follow the same field policy. A sidecar that ships every prompt to an open log group is a second copy of the corpus. Metadata on the service log; raw prompts only in the restricted store.
