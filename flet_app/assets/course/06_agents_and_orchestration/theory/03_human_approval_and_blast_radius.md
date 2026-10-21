# Human Approval and Blast Radius

Autonomy is a blast-radius decision. The interesting question is not "can the model click the button." It is what a wrong click costs, and whether a second click is possible.

## The gate

`approval_gate(side_effect, prod, amount_usd)` returns true when a person must confirm before the tool runs.

| Condition | Approval |
|-----------|----------|
| Unknown side effect, or `amount_usd < 0` | `ValueError` |
| `read` | False. Do not page a human to look something up |
| `irreversible` | True, in prod and in lower environments. Rehearsing deletes without a gate trains the wrong habit |
| `write` in prod at `amount_usd >= 1000` | True |
| `write` at `amount_usd >= 10000` even outside prod | True. A large test payment is still a payment |
| Other writes | False. The tool is still idempotent and authorized |

```python
def approval_gate(side_effect, prod, amount_usd) -> bool:
    if side_effect not in {"read", "write", "irreversible"} or amount_usd < 0:
        raise ValueError("bad input")
    if side_effect == "read":
        return False
    if side_effect == "irreversible":
        return True
    if prod and amount_usd >= 1000:
        return True
    if amount_usd >= 10000:
        return True
    return False
```

Amounts are a stand-in for impact. A write that exports a customer list is irreversible-class even if the dollar figure is zero — classify the side effect honestly, do not hide it as a cheap write.

## Where the human sits

| Place | Fits |
|-------|------|
| Step Functions callback (`.waitForTaskToken`) | The durable choice. The model call can end; the approval lives |
| In-chat button that calls your API | Fine for low latency if the token is the approval, not a sentence the model utters |
| "The model said the user agreed" | Not an approval |

The approver sees the tool name, the arguments, the tenant, and the idempotency key. They do not see a paragraph asking them to trust the assistant. After approval, the workflow executes the tool. The agent does not get a second chance to edit the arguments.

Review line: **"Approval binds arguments. A later model turn does not get to amend them."**

## Blast radius checklist

- Per-tool IAM, not a general agent role
- Per-tenant rate limits on write tools
- A kill switch that disables action groups without redeploying the model
- A maximum hop count and a maximum tool-call budget per turn
- Production aliases separate from draft agents
