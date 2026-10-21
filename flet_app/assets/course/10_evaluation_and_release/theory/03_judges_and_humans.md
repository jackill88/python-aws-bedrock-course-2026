# Judges and Humans

An LLM judging an LLM is cheap and circular if you never calibrate it. Humans are slow and also biased. The architect assigns the method to the claim.

## The assignment

`judge_trust(task)`:

| Task | Method |
|------|--------|
| `format_compliance` | `automatic_ok` — a parser is the judge |
| `groundedness_against_sources` | `model_judge_plus_audit_sample` — a model can compare claim to passage, and a human sample checks the judge |
| `helpfulness` | `human_sample` — preference is not a unit test |
| `policy_violation` | `automatic_plus_human_on_positive` — automatic flags are reviewed by a person; you do not auto-punish or auto-ship on the flag alone |
| Anything else | `ValueError` |

```python
def judge_trust(task: str) -> str:
    methods = {
        "format_compliance": "automatic_ok",
        "groundedness_against_sources": "model_judge_plus_audit_sample",
        "helpfulness": "human_sample",
        "policy_violation": "automatic_plus_human_on_positive",
    }
    if task not in methods:
        raise ValueError("unknown task")
    return methods[task]
```

## Rules that keep judges honest

| Rule | Why |
|------|-----|
| The judge model is not the candidate model | Shared failure modes look like agreement |
| The judge sees the passages for grounding | A judge without sources scores fluency |
| Audit a fixed sample of judge decisions each cycle | Drift in the judge is a silent gate failure |
| Humans see randomized, blinded pairs when comparing two prompts | Order bias is real |
| Policy positives get a person | False flags and missed flags both matter, and automation is better at volume than at edge cases |

Bedrock human-evaluation workflows fit the `human_sample` and the audit sample. They do not replace the decision about which tasks are allowed to be automatic.

Review line: **"A judge score without an audit sample is a rumor with a decimal."**
