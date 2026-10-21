# Private Network Paths

Bedrock runtime is a public AWS API until you decide it is not, for your VPC. Interface VPC endpoints (PrivateLink) exist for the runtime, the control plane, and the agent and knowledge-base runtimes you actually use. Creating the endpoint is the customer's job (Module 01).

## The rule

`network_path(data_class)`:

| Data class | Path |
|------------|------|
| `public` | `public_endpoint_ok` |
| `confidential` or `restricted` | `interface_vpc_endpoint` |
| Anything else | `ValueError` |

Public marketing copy and a sandbox with synthetic prompts may use the public endpoint. Customer content, employee data, and anything you marked restricted do not traverse the public path from your VPC. "The API is TLS" is true and incomplete: TLS does not give you a private route, a VPC endpoint policy, or a security group.

```python
def network_path(data_class: str) -> str:
    if data_class == "public":
        return "public_endpoint_ok"
    if data_class in {"confidential", "restricted"}:
        return "interface_vpc_endpoint"
    raise ValueError("unknown data class")
```

## What to stand up

| Endpoint | When |
|----------|------|
| `bedrock-runtime` | Any private invoke or converse path |
| `bedrock` | Control-plane calls from a private pipeline, if those calls must not use the public API |
| `bedrock-agent-runtime` | Private agent invocation |
| Knowledge base / agent endpoints you call | Same rule as the data class of the prompts they see |

Then:

1. Endpoint policy limited to your model and knowledge-base ARNs, not `*`.
2. Security groups that accept 443 only from the application subnets.
3. A guardrail in the account's egress design so the task subnet cannot reach the public Bedrock endpoint as a bypass. Private DNS on the endpoint is the usual way. Test the bypass; do not assume it.
4. The same pattern for S3 (corpus, logs) and for the vector store. A private Bedrock path with a public OpenSearch dashboard is a half design.

Review line: **"Draw the packet. If restricted text can still hairpin out to the public API, the endpoint is decorative."**

Third-party vector stores and Marketplace models may leave the VPC by another door. Name that door in the data-flow diagram or do not send restricted text there.
