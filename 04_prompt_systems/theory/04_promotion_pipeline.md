# Promotion Pipeline

A prompt version is promoted when four gates pass, not when the author likes the tone. `promote_prompt` returns `"promote"` or `"hold"`.

| Gate | Pass condition |
|------|----------------|
| Offline score | `offline_score >= 0.85` on the frozen set. The score is in `[0, 1]` or the function raises `ValueError` |
| Regression | `regression` is false. Any tracked metric moving the wrong way holds the release |
| Injection suite | `injection_suite_passed` is true |
| Human review | `human_review` is true for this course's production gate |

```python
def promote_prompt(offline_score, regression, injection_suite_passed, human_review) -> str:
    if not 0.0 <= offline_score <= 1.0:
        raise ValueError("score out of range")
    if (
        offline_score >= 0.85
        and not regression
        and injection_suite_passed
        and human_review
    ):
        return "promote"
    return "hold"
```

Missing a gate is a hold, not an exception. An out-of-range score is a broken pipeline and should fail loudly.

## What the offline score is

Module 10 defines the metrics. For the promotion function, the score is a single number your platform already computed: the fraction of eval cases that met the use-case bar. Do not average a safety failure with a style win and call it 0.9. If the safety suite failed, `injection_suite_passed` is false even if the quality score is high. The gates are independent on purpose.

## Human review

Human review here is a recorded approval of **this version**, not a permanent waiver for the author. The record stores the version id, the eval run id, and the approver. Platform admins can roll back without that approver present.

For a pure classifier with no safety content, you might later relax the human gate. This course keeps it, because the point of the exercise is that production prompts do not auto-promote from a notebook.

## After promotion

| Event | Action |
|-------|--------|
| Promote | Pin the gateway to the new version. Keep the previous pin for immediate rollback |
| Quality drop on live traffic | Roll back the pin. Do not hot-edit the text |
| Model id change | New promotion. The old score does not transfer |
| Guardrail version change | New promotion if the user-visible refusal behavior changes |

Review line: **"The live prompt version is an output of CI, the same way a container image is."**

Shadow traffic — running the candidate beside production without showing it — is how you earn the right to lower fear of the 0.85 bar. It is not a bypass. Module 10 ties shadow deltas to the release gate for model changes; prompt changes use the same muscle.
