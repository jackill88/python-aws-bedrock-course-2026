# Module 04: Prompt Systems

A prompt in production is a versioned artifact with a trust boundary and a promotion gate. It is not a string someone edits in a console during an incident.

## Learning Objectives

By the end of this module you will be able to:

- Separate trusted instructions from untrusted user, retrieval, and tool text
- Treat tool schemas and structured output as contracts
- Require an eval, an injection suite, and a human review before a prompt version is promoted
- Say where business policy must stay out of the model

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Prompts as Artifacts | [theory/01_prompts_as_artifacts.md](theory/01_prompts_as_artifacts.md) |
| 2 | Structured Output and Tool Schemas | [theory/02_structured_output_and_tools.md](theory/02_structured_output_and_tools.md) |
| 3 | Trust Boundaries and Injection | [theory/03_trust_boundaries_and_injection.md](theory/03_trust_boundaries_and_injection.md) |
| 4 | Promotion Pipeline | [theory/04_promotion_pipeline.md](theory/04_promotion_pipeline.md) |

## Quiz

Test your understanding: [quizzes/prompt_systems_quiz.md](quizzes/prompt_systems_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Trust Zone | [challenges/trust_zone.py](challenges/trust_zone.py) |
| Promote Prompt | [challenges/promote_prompt.py](challenges/promote_prompt.py) |
| Required Fields Present | [challenges/required_fields_present.py](challenges/required_fields_present.py) |

Run tests for this module:

```bash
pytest tests/04_prompt_systems/ -v
```
