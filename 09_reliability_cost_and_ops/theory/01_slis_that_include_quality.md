# SLIs That Include Quality

Classic SLIs still apply: availability of the invoke path, latency, error rate, saturation of your quota. A generative system adds quality SLIs, or the dashboard stays green while the product lies.

## Three signals

`slo_status(availability, groundedness, p95_ms, targets)` compares a window to a target dict with keys `availability`, `groundedness`, and `p95_ms`.

| Breach | When |
|--------|------|
| None → `met` | Availability and groundedness are at least their targets, and p95 latency is at most its target |
| `availability_breach` | Availability is the only miss |
| `quality_breach` | Groundedness is the only miss |
| `latency_breach` | p95 is the only miss |
| `multi_breach` | More than one miss |

Missing target keys raise `ValueError`. Do not treat a missing target as "no target, so pass."

```python
def slo_status(availability, groundedness, p95_ms, targets) -> str:
    required = ("availability", "groundedness", "p95_ms")
    if any(key not in targets for key in required):
        raise ValueError("incomplete targets")
    breaches = []
    if availability < targets["availability"]:
        breaches.append("availability")
    if groundedness < targets["groundedness"]:
        breaches.append("quality")
    if p95_ms > targets["p95_ms"]:
        breaches.append("latency")
    if not breaches:
        return "met"
    if len(breaches) > 1:
        return "multi_breach"
    return breaches[0] + "_breach"
```

Availability here means "the gateway returned a deliberate outcome": a normal answer, a grounded abstain, or a guardrail refusal. A timeout, a 5xx, and an uncaught throttle past the retry budget count against availability. An abstain that followed the citation policy does **not**. It counts in a separate "answer rate" product metric so you notice a retrieval outage that abstains perfectly and helps nobody.

## Error budgets

Spend the budget on purpose. A quality breach and a latency breach should not share one number if the responses differ: quality breaches roll back a prompt or a model; latency breaches shed load or add capacity. `multi_breach` means you do not get to pick the flattering explanation.

Review line: **"A refused answer inside policy is success. A fluent answer outside the corpus is not."**

Set groundedness from Module 07's ratio (often 0.9 for policy answers) and latency from the budget in Module 11. Write both numbers before the launch review, not after the first complaint.
