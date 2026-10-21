# Structured Output and Tool Schemas

Free text is a user interface. JSON that another service parses is an API. Lead architects do not "ask the model nicely" for the second one and hope.

## Two different contracts

| Need | Mechanism |
|------|-----------|
| A person will read the answer | Prose, plus citations if the path is RAG. Still length-capped |
| A service will branch on the answer | A schema: required fields, enums, types. Validate before you branch |
| The model must call a system | A tool schema. The tool implementation checks authorization again |

Converse tool use is the supported way to get structured tool calls. For structured answers with no side effect, prefer a tool or a constrained decode the model supports over a paragraph you slice with regular expressions.

## Validate in your code

`required_fields_present(payload, required)` is the smallest gate: every listed key exists and is not `None`. An empty `required` list passes. This does not replace a full JSON Schema check; it is the habit the gateway refuses to skip.

```python
def required_fields_present(payload: dict, required: list[str]) -> bool:
    return all(key in payload and payload[key] is not None for key in required)
```

On failure, do not send the payload to the tool. You may retry the model **once** with the validation error as a tool result or a follow-up turn. A second failure is a fallback message, not a loop.

## Tool schema rules

| Rule | Why |
|------|-----|
| The schema is versioned with the tool, not invented in the prompt | Module 02: it is a contract |
| The model chooses arguments; your code authorizes them | The model is not an IAM principal |
| Enums are closed | Open strings become injection into downstream queries |
| Idempotency keys are arguments on write tools | Retries and agent replays |
| Descriptions are short and stable | They sit in the cached prefix |

A tool named `run_sql` with a raw query string is not a tool schema. It is a remote shell. Expose narrow operations: `get_order(order_id)`, `search_policy(query, tenant_id)` where `tenant_id` is set by the gateway, not by the model.

Review line: **"The model proposes a tool call. The application disposes."**

## Business policy stays in the application

Refund thresholds, entitlement checks, and "this user is a minor" are not prompt paragraphs you hope the model obeys. They are code on the tool path. The prompt may explain the policy to the user. The tool enforces it. `abstraction_boundary("business_policy")` returns `application` for that reason.
