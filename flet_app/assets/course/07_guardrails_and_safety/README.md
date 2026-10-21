# Module 07: Guardrails and Safety

Amazon Bedrock Guardrails are a policy layer on the model call: content filters, denied topics, word filters, sensitive-information handling, and contextual grounding. They are not the product's only control, and they do not understand your tenants.

## Learning Objectives

By the end of this module you will be able to:

- Place checks on the right surface: user chat, tool arguments, grounded answers, batch output
- Choose block, mask, allow, or redact for PII by entity and audience
- Fail a groundedness bar when supported claims fall below a ratio
- Stack guardrails with application policy instead of hoping one filter covers injection and authorization

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Where Guardrails Sit | [theory/01_guardrail_placement.md](theory/01_guardrail_placement.md) |
| 2 | Topics, Words, and PII | [theory/02_topics_words_and_pii.md](theory/02_topics_words_and_pii.md) |
| 3 | Contextual Grounding | [theory/03_contextual_grounding.md](theory/03_contextual_grounding.md) |
| 4 | Defense in Depth | [theory/04_defense_in_depth.md](theory/04_defense_in_depth.md) |

## Quiz

Test your understanding: [quizzes/guardrails_safety_quiz.md](quizzes/guardrails_safety_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Guardrail Stages | [challenges/guardrail_stages.py](challenges/guardrail_stages.py) |
| PII Action | [challenges/pii_action.py](challenges/pii_action.py) |
| Grounding Verdict | [challenges/grounding_verdict.py](challenges/grounding_verdict.py) |

Run tests for this module:

```bash
pytest tests/07_guardrails_and_safety/ -v
```
