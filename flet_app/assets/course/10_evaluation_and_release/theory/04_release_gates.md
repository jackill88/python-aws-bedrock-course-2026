# Release Gates

`release_decision(offline, safety_passed, cost_increase_pct, shadow_quality_delta)` returns `ship` or `block`. `shadow_quality_delta` is candidate minus current. Negative means the shadow got worse.

| Order | Result |
|-------|--------|
| `offline` outside `[0, 1]` | `ValueError` |
| `safety_passed` is false | `block` |
| `offline < 0.8` | `block` |
| `shadow_quality_delta <= -0.02` | `block` (a two-point drop is enough) |
| Cost increase above 25% and the quality delta is below `0.05` | `block` — you are paying more without a meaningful gain |
| Otherwise | `ship` |

```python
def release_decision(offline, safety_passed, cost_increase_pct, shadow_quality_delta) -> str:
    if not 0 <= offline <= 1:
        raise ValueError("offline out of range")
    if not safety_passed or offline < 0.8 or shadow_quality_delta <= -0.02:
        return "block"
    if cost_increase_pct > 25 and shadow_quality_delta < 0.05:
        return "block"
    return "ship"
```

A large quality gain may justify a large cost increase. A tiny gain may not. Safety never trades against either. The prompt-promotion gate in Module 04 is stricter on the human checkbox and the 0.85 bar because it is the prompt's own pipeline. This function is the **model or platform release** gate: same muscle, explicit cost and shadow inputs.

## After the gate says ship

| Step | Done when |
|------|-----------|
| Pin the candidate | Gateway config shows the new ids |
| Watch the SLIs from Module 09 | A short bake window with rollback authority staffed |
| Keep the previous pin | Rollback does not require a build |
| Record the eval run id | The release ticket links the score to the artifact |

Shadow that you do not actually compare is not a gate. If the shadow path cannot see production-shaped prompts under the logging policy, say so and use an approved sample, not a bypass that copies raw production text into a personal bucket.

Review line: **"Safety blocks. A two-point shadow drop blocks. A cost jump needs a quality reason."**
