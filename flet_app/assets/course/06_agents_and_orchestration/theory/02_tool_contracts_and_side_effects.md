# Tool Contracts and Side Effects

A tool is an API with a model as one of the callers. The model is untrusted (Module 04). The implementation authorizes, validates, and is idempotent when it writes.

## Side effects

`tool_idempotency_key(side_effect)`:

| Side effect | Key |
|-------------|-----|
| `read` | `none_required` |
| `write` or `irreversible` | `required` |
| Anything else | `ValueError` |

Reads can be repeated. Writes and irreversible actions (send the email, place the order, delete the record, pay the invoice) must accept a caller-generated idempotency key so an agent retry or a workflow replay does not double-apply. The key is minted by the gateway for the user turn, not invented by the model each hop. If the model can mint a new key on every retry, the key does nothing.

## Shape of a safe tool

| Property | Read tool | Write tool |
|----------|-----------|------------|
| Authorization | Re-check the caller's scope. Ignore ids the model added for other tenants | Same, plus the idempotency key |
| Schema | Closed identifiers, not raw queries | Same |
| Timeout | Short. A hung read blocks the loop | Short, and the workflow knows whether the call landed |
| Result returned to the model | The minimum the next hop needs. Redact secrets | An id and a status, not a dump of the new record |
| Trace | Tool name, latency, error | Plus idempotency key and the human approval id if any |

Review line: **"The idempotency key is minted once per user action. The model does not get to roll a new one."**

## Action groups versus in-process tools

Bedrock Agents invoke Lambda or return control. Lambda in the agent's account is convenient and easy to over-privilege. Prefer:

- A separate execution role per action group, scoped to one system
- Return of control for anything in a private VPC or behind a human
- No shared "utility" Lambda that can both read the knowledge base credentials and call payments

OpenAPI specifications imported as action groups drift. Version them with the agent alias. An alias is how you shift traffic; editing the draft agent in place is how you surprise production.
