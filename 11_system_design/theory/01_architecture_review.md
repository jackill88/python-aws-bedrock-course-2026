# How to Run the Review

A Bedrock review is a sequence. Skipping to the model name is how the tenancy bug survives until production.

## Order

1. **Users and data classes.** Who asks, what text moves, public / confidential / restricted.
2. **Task shape.** Read-only answer, structured extraction, or a tool that writes.
3. **Grounding.** Prompt, long context, RAG, fine-tune, or a combination (Module 05).
4. **Orchestration.** Workflow, agent, hybrid, or human approval (Module 06).
5. **Regions.** Caller, inference-profile destinations, index, logs (Module 08).
6. **Identity.** Runtime role versus platform role. No `bedrock:*`.
7. **Quality bar.** Groundedness, abstain, safety suite, and the release gate.
8. **Numbers.** Latency budget, steady and peak rate, cost ceiling per tenant.
9. **Failure.** Throttle, empty retrieval, bad prompt pin, region loss. The mitigation is a pin, a fallback you measured, or an abstain — named in the ticket.

If the proposal cannot fill a row, the review outcome is "not ready," not "approved with a follow-up to think about IAM."

## Tenancy language

`tenancy_model(isolation, tenants)` uses the case-study vocabulary. It matches Module 05's classes:

| Isolation | Module 05 name | Result |
|-----------|----------------|--------|
| `tenants < 1` | — | `ValueError` |
| `regulatory` | `regulated_plus` | `account_per_tenant` |
| `strong` | `strict` | `index_per_tenant` |
| `logical` | `standard` | `shared_index_metadata_filter` |
| Other | — | `ValueError` |

Tenant count must be a positive integer and **does not** downgrade isolation. A platform that "will start shared and split later" for regulatory data is proposing to leak first. Say so.

```python
def tenancy_model(isolation: str, tenants: int) -> str:
    if tenants < 1:
        raise ValueError("tenant count")
    if isolation == "regulatory":
        return "account_per_tenant"
    if isolation == "strong":
        return "index_per_tenant"
    if isolation == "logical":
        return "shared_index_metadata_filter"
    raise ValueError("unknown isolation")
```

Review line: **"Isolation class first. Cost is a consequence you staff, not a reason to share a regulated index."**
