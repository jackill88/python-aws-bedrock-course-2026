# Lambda

Use Lambda when `choose_compute` says so: one invocation, done within the platform ceiling, no session pinned to the process. The usual Bedrock shapes are a synchronous `Converse` from API Gateway or a function URL, a queue consumer, and an agent action group.

## Edges, not the function timeout

The function timeout can be 15 minutes. The front door is often stricter. `platform_timeout_s` returns that ceiling in seconds:

| Edge | Ceiling | Why |
|------|---------|-----|
| `api_gateway` | 29 | REST integration timeout. HTTP APIs stop at 30 seconds, so this course uses 29 as the ceiling you must fit. A 45-second model call is cut off here even if Lambda is still running |
| `lambda_function_url` | 900 | The function's own maximum. Response streaming fits here when the stream finishes in time |
| `alb` | 4000 | The maximum idle timeout you can set. The default is 60 seconds; a stream dies at the default unless you raise it |
| `ecs_task` | `None` | No AWS cap of this kind. The deadline is the one you configure on the task, the client, and the load balancer |
| Anything else | `ValueError` | |

```python
def platform_timeout_s(edge: str) -> int | None:
    ceilings = {
        "api_gateway": 29,
        "lambda_function_url": 900,
        "alb": 4000,
        "ecs_task": None,
    }
    if edge not in ceilings:
        raise ValueError("unknown edge")
    return ceilings[edge]
```

If the p95 Bedrock path, including retrieval and guardrails, does not fit under the edge you picked, change the edge. Do not raise the Lambda timeout and hope API Gateway notices.

Set three clocks in order, longest last: the model/SDK read timeout, then the Lambda timeout, then a client deadline that is shorter than the edge. A Lambda timeout that fires while the SDK is still reading leaves an unknown outcome. Module 03's retry rule still applies: a timeout after a non-idempotent tool is not a blind retry.

## Action groups

Bedrock Agents invoke an action-group function **synchronously**. Keep that function to one checked tool call. Do not hide a second agent loop inside it. The agent's execution role may call the function; the function's role may call Bedrock or the downstream API, not both with `*`. Return of control (Module 06) remains the alternative when the tool must run in your VPC under a human approval instead of inside the agent's invoke.

## Asynchronous retries

Lambda retries a failed **asynchronous** invocation twice. That is a second and third `Converse`, and a second tool execution if the function got far enough. `async_duplicate_risk(invoke_mode, side_effect)`:

| Invoke mode | Side effect | Result |
|-------------|-------------|--------|
| Unknown mode or side effect | | `ValueError` |
| `sync` | read, write, or irreversible | `client_retries_only` |
| `async` | `read` | `duplicate_model_call` |
| `async` | `write` or `irreversible` | `duplicate_side_effect` |

```python
def async_duplicate_risk(invoke_mode: str, side_effect: str) -> str:
    if invoke_mode not in {"sync", "async"} or side_effect not in {"read", "write", "irreversible"}:
        raise ValueError("bad invoke or side effect")
    if invoke_mode == "sync":
        return "client_retries_only"
    if side_effect == "read":
        return "duplicate_model_call"
    return "duplicate_side_effect"
```

`client_retries_only` means the platform will not add those two attempts. The caller, API Gateway's client, or your own code still might. Synchronous does not mean idempotent. `duplicate_side_effect` means you need the gateway-minted idempotency key from Module 06, or you should not use async invoke for that tool.

SQS is different from Lambda's async invoke API: you control the visibility timeout and the redrive. Set the visibility timeout longer than the function timeout so a slow Bedrock call is not delivered twice while the first is still running.

## VPC and concurrency

Confidential or restricted prompts use the interface endpoint for `bedrock-runtime` (Module 08). A Lambda in a private subnet needs that endpoint, a security group that can reach it, and a cold-start story you have measured. Provisioned concurrency is how you pay for warmth **without** moving a short stateless call to ECS.

Reserved concurrency on the function that calls Bedrock caps a retry storm so this one use case cannot consume the account's Lambda concurrency. It does not raise the Bedrock quota. Those are different ceilings (Module 09).
