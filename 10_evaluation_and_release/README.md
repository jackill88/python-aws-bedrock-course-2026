# Module 10: Evaluation and Release

A model or prompt change is a release. Lead architects define the offline set, what a judge is allowed to decide, and the gate that blocks a ship when safety, quality, or cost moves the wrong way.

## Learning Objectives

By the end of this module you will be able to:

- Compute recall at k for a retrieval change
- Match the evaluation method to the claim: format, grounding, helpfulness, policy
- Block a release on safety, offline score, shadow regression, or an unjustified cost jump
- Keep human review where automatic scores are weakest

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | The Evaluation Pyramid | [theory/01_evaluation_pyramid.md](theory/01_evaluation_pyramid.md) |
| 2 | RAG and Agent Metrics | [theory/02_rag_and_agent_metrics.md](theory/02_rag_and_agent_metrics.md) |
| 3 | Judges and Humans | [theory/03_judges_and_humans.md](theory/03_judges_and_humans.md) |
| 4 | Release Gates | [theory/04_release_gates.md](theory/04_release_gates.md) |

## Quiz

Test your understanding: [quizzes/evaluation_release_quiz.md](quizzes/evaluation_release_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Recall at K | [challenges/recall_at_k.py](challenges/recall_at_k.py) |
| Judge Trust | [challenges/judge_trust.py](challenges/judge_trust.py) |
| Release Decision | [challenges/release_decision.py](challenges/release_decision.py) |

Run tests for this module:

```bash
pytest tests/10_evaluation_and_release/ -v
```
