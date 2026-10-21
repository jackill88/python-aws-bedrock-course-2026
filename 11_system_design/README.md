# Module 11: System Design

This module is the review you run on a real proposal: a tenancy choice, a latency budget that adds up, and a pattern for four cases that show up constantly — policy Q&A, regulated decisions, operations agents, and a shared platform.

## Learning Objectives

By the end of this module you will be able to:

- Run a Bedrock architecture review in a fixed order
- Map isolation needs to account, index, or shared-filter tenancy without letting tenant count weaken the class
- Allocate a user-visible latency budget across retrieval, rerank, model, generation, and guardrails
- Name the pattern for the four reference cases

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | How to Run the Review | [theory/01_architecture_review.md](theory/01_architecture_review.md) |
| 2 | Enterprise Knowledge Assistant | [theory/02_enterprise_knowledge_assistant.md](theory/02_enterprise_knowledge_assistant.md) |
| 3 | Regulated Workflow and Operations Agent | [theory/03_regulated_workflow_and_ops_agent.md](theory/03_regulated_workflow_and_ops_agent.md) |
| 4 | Shared Platform Blueprint | [theory/04_shared_platform_blueprint.md](theory/04_shared_platform_blueprint.md) |

## Quiz

Test your understanding: [quizzes/system_design_quiz.md](quizzes/system_design_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Tenancy Model | [challenges/tenancy_model.py](challenges/tenancy_model.py) |
| Latency Budget | [challenges/latency_budget.py](challenges/latency_budget.py) |
| Case Pattern | [challenges/case_pattern.py](challenges/case_pattern.py) |

Run tests for this module:

```bash
pytest tests/11_system_design/ -v
```
