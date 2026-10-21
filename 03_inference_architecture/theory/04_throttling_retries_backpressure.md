# Throttling, Retries, and Backpressure

Retries are how a small incident becomes a quota collapse. The gateway retries only the errors that can succeed on a later attempt, with a cap, with jitter, and only when repeating the call is safe.

## The decision

`retry_decision(error_code, attempt, max_attempts, idempotent)` uses the attempt that **just failed** (1-based). `max_attempts` is the maximum number of tries, not the maximum number of retries. Attempt 3 of 3 does not schedule a fourth try.

| Condition | Result |
|-----------|--------|
| `attempt < 1` or `max_attempts < 1` | `ValueError` |
| `ValidationException` or `AccessDeniedException` | `fail` immediately, even if attempts remain |
| Any other unknown code | `ValueError` |
| `attempt >= max_attempts` | `fail` |
| `ThrottlingException` and attempts remain | `retry` |
| `ModelTimeoutException`, `InternalServerException`, or `ServiceUnavailableException`, attempts remain, and `idempotent` | `retry` |
| Those transient codes when the call is not idempotent | `fail` |

Throttle retries do not require `idempotent`. A throttled call did not execute. A timeout might have executed far enough to run a tool — if you are not sure, `idempotent=False` and you fail closed.

```python
FAIL_CLOSED = {"ValidationException", "AccessDeniedException"}
TRANSIENT = {
    "ModelTimeoutException",
    "InternalServerException",
    "ServiceUnavailableException",
}

def retry_decision(error_code, attempt, max_attempts, idempotent) -> str:
    if attempt < 1 or max_attempts < 1:
        raise ValueError("attempt counts must be positive")
    if error_code in FAIL_CLOSED:
        return "fail"
    if error_code != "ThrottlingException" and error_code not in TRANSIENT:
        raise ValueError("unknown error")
    if attempt >= max_attempts:
        return "fail"
    if error_code == "ThrottlingException":
        return "retry"
    return "retry" if idempotent else "fail"
```

Backoff itself (full jitter, a cap of a few seconds, a budget shared with the client deadline) sits around this decision. The function only answers retry or fail.

## Backpressure

When retries are exhausted or the tenant is over budget:

| Mechanism | Effect |
|-----------|--------|
| Per-tenant token bucket | One product cannot consume the account quota |
| Queue for batchable work | Interactive traffic stays on-demand; overflow becomes a job |
| Load shedding | Return a clear "try later" before you call the model |
| Provisioned throughput | Buy a floor for the steady path (Module 01 and 09) |

Do not retry `ServiceQuotaExceededException` in a tight loop inside the request. That error means the ceiling is gone for the minute. Shed or queue. This challenge treats quota exhaustion as unknown on purpose — it is not an automatic retry. Module 02 routes it to same-model backoff at the **policy** layer, which may mean "delay the job," not "spin inside the user request."

Review line: **"The user request gets one bounded retry policy. The backlog gets a queue."**
