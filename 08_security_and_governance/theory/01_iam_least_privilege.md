# IAM Least Privilege

`bedrock:*` on `*` is how a prototype ships and how a review fails. Split the platform role from the runtime role, and split production invoke from dev invoke.

## The matrix

`authorize(role, action)` returns `allow` or `deny`. Unknown role or unknown action raises `ValueError`.

| Action | platform_admin | app_runtime | data_scientist | auditor | product_dev |
|--------|----------------|-------------|----------------|---------|-------------|
| `invoke_prod` | allow | allow | deny | deny | deny |
| `invoke_dev` | allow | deny | allow | deny | allow |
| `create_guardrail` | allow | deny | deny | deny | deny |
| `read_invocation_logs` | allow | deny | allow | allow | deny |
| `manage_provisioned_throughput` | allow | deny | deny | deny | deny |
| `retrieve_kb` | allow | allow | deny | deny | deny |

```python
ROLES = {
    "platform_admin": {
        "invoke_prod", "invoke_dev", "create_guardrail",
        "read_invocation_logs", "manage_provisioned_throughput", "retrieve_kb",
    },
    "app_runtime": {"invoke_prod", "retrieve_kb"},
    "data_scientist": {"invoke_dev", "read_invocation_logs"},
    "auditor": {"read_invocation_logs"},
    "product_dev": {"invoke_dev"},
}
ACTIONS = {
    "invoke_prod", "invoke_dev", "create_guardrail",
    "read_invocation_logs", "manage_provisioned_throughput", "retrieve_kb",
}

def authorize(role: str, action: str) -> str:
    if role not in ROLES or action not in ACTIONS:
        raise ValueError("unknown role or action")
    return "allow" if action in ROLES[role] else "deny"
```

The runtime can invoke production and retrieve from the knowledge base. It cannot read the full invocation log, create guardrails, or buy provisioned throughput. Scientists and product developers share the **dev** model path. Only the scientist role and the auditor read logs, and the scientist still cannot invoke production. If a scientist needs a production trace, they get a time-bound auditor path, not a permanent `invoke_prod`.

## Resource ARNs

Actions are necessary and not sufficient. `InvokeModel` and `Converse` are authorized against **foundation-model and inference-profile ARNs**. `Retrieve` is authorized against the knowledge-base ARN. A policy that allows `invoke_prod` in this exercise still needs, in AWS, a resource list limited to the approved model ids. An allow on `arn:aws:bedrock:*::foundation-model/*` is the same mistake as `bedrock:*`, one level down.

Guardrail and agent aliases are resources too. Passing the id in the request does not authorize it; IAM does, if you constrained the resource.

Review line: **"The runtime role's policy fits on one screen, with model ARNs named."**

## SCPs

Service control policies belong on the organization, not in the app. Typical denies: Bedrock in regions you do not use, Marketplace model subscriptions in production accounts, and `bedrock:InvokeModel` from accounts that are not the platform or the approved app accounts. SCPs are a backstop. They are not a substitute for the runtime policy, because an SCP that allows a region still allows every model in it.
