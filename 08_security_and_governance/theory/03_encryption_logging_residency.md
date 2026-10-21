# Encryption, Logging, and Residency

Encryption in transit is shared (Module 01). Encryption at rest for custom models and for the logs you create is a KMS decision: AWS-owned keys are the easy default; a customer-managed key is what you want when audit requires a key policy you control and a revocation story you can explain. Do not invent a CMK for its own sake and then grant every role `kms:Decrypt`.

## Log fields

Model invocation logging can store prompts and completions in CloudWatch Logs and/or S3. That store is a copy of customer text. `log_field_policy(field)`:

| Field | Policy |
|-------|--------|
| `request_id`, `model_id`, `latency_ms`, `token_counts` | `keep` |
| `prompt`, `completion`, `retrieved_text` | `redact_or_separate_restricted_store` |
| `api_key`, `authorization` | `drop` |
| Anything else | `ValueError` |

Operational dashboards get the `keep` fields in the hot account. Raw prompts, if you truly need them for eval or abuse review, go to a restricted bucket with a short retention, a CMK, and the auditor role from the IAM matrix. They do not go to the application log group that every developer can tail. Authorization headers never get logged, including "just in debug."

```python
def log_field_policy(field: str) -> str:
    if field in {"request_id", "model_id", "latency_ms", "token_counts"}:
        return "keep"
    if field in {"prompt", "completion", "retrieved_text"}:
        return "redact_or_separate_restricted_store"
    if field in {"api_key", "authorization"}:
        return "drop"
    raise ValueError("unknown field")
```

CloudTrail remains the control-plane audit. It is not a substitute for this policy, and this policy is not a substitute for CloudTrail.

## Residency

`residency_allowed(processing_regions, allowed_regions)` is true only when **every** processing region is in the allowed set. An empty processing list is **false**: unknown is not allowed. Order does not matter. Duplicates are fine.

```python
def residency_allowed(processing_regions: list[str], allowed_regions: list[str]) -> bool:
    if not processing_regions:
        return False
    allowed = set(allowed_regions)
    return all(region in allowed for region in processing_regions)
```

Build `processing_regions` from:

- The region you call
- Every destination on a cross-region inference profile
- The region of the knowledge base, the vector store, the log bucket, and the CMK

A profile that fails over to a region outside the list is a residency bug even if the SDK call was made in an allowed region. If the list is empty because "the vendor is global," the function returns false until someone writes the real list down.

Review line: **"No profile destination that is not on the allowed-region list. No empty list."**
