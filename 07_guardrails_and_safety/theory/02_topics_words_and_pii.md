# Topics, Words, and PII

Bedrock Guardrails can deny topics, filter harmful content categories at a strength you choose, block or mask words, and detect sensitive information such as email addresses, phone numbers, and identifiers you configure. The architect's job is the **action** per entity and audience, not the longest block list.

## Actions

`pii_action(entity, audience)`:

| Audience | email, phone | ssn | name |
|----------|--------------|-----|------|
| `logs` | redact | redact | redact |
| `internal_support` | mask | mask | allow |
| `external_user` | mask | block | mask |

Unknown entity or audience raises `ValueError`. Entities are `email`, `ssn`, `name`, `phone`. Audiences are `internal_support`, `external_user`, `logs`.

Logs are the widest audience over time, so they are the strictest: redact all four. Support staff may see a customer's name and a masked national identifier; they do not get the raw SSN in the tool result that will be pasted back into the transcript. External users never receive an SSN, even masked, in this policy — the call is blocked. Masking an email in a user-visible reply is usually enough; blocking every email breaks legitimate "send this to me" flows.

```python
def pii_action(entity: str, audience: str) -> str:
    entities = {"email", "ssn", "name", "phone"}
    audiences = {"internal_support", "external_user", "logs"}
    if entity not in entities or audience not in audiences:
        raise ValueError("unknown entity or audience")
    if audience == "logs":
        return "redact"
    if entity == "ssn" and audience == "external_user":
        return "block"
    if entity == "ssn":
        return "mask"
    if entity == "name" and audience == "internal_support":
        return "allow"
    if entity == "name":
        return "mask"
    return "mask"  # email, phone
```

## Denied topics versus content filters

| Control | Good at | Weak at |
|---------|---------|---------|
| Content filters | Standard harm categories at a chosen strength | Your internal "do not give legal advice" rule |
| Denied topics | A described subject you must refuse | A topic you defined so vaguely that it fires on the help center |
| Word filters | Known codes, slurs, competitor names you must not emit | Paraphrase |
| This table's PII policy | Consistent handling by audience | Detecting secrets that do not match a detector |

Write denied topics as behaviors ("instructions for evading the company's identity verification"), not as single nouns that appear in benign documents. Test them on the real corpus. A topic that fires on the employee handbook will train users to route around the assistant.

Review line: **"Block strength is a product decision. Measure false refuses on the eval set before you turn the dial up."**
