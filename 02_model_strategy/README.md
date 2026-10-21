# Module 02: Model Strategy

Pick a **class** of model, a routing policy, and an exit plan. Naming a single model id in the architecture review is the beginning of the decision, not the end.

## Learning Objectives

By the end of this module you will be able to:

- Map a task to a small, balanced, or frontier tier without turning the review into a vendor bake-off
- Separate throttle retries from fallback to another model
- Keep model ids, prompts, and tool schemas behind the right change boundary
- Explain what lock-in looks like on a managed multi-model platform

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Selection Axes | [theory/01_selection_axes.md](theory/01_selection_axes.md) |
| 2 | Routing, Fallback, and Pinning | [theory/02_routing_fallback_and_pinning.md](theory/02_routing_fallback_and_pinning.md) |
| 3 | Lifecycle and Lock-in | [theory/03_lifecycle_and_lock_in.md](theory/03_lifecycle_and_lock_in.md) |
| 4 | Modalities and Context | [theory/04_modalities_and_context.md](theory/04_modalities_and_context.md) |

## Quiz

Test your understanding: [quizzes/model_strategy_quiz.md](quizzes/model_strategy_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Select Model Tier | [challenges/select_model_tier.py](challenges/select_model_tier.py) |
| Fallback Route | [challenges/fallback_route.py](challenges/fallback_route.py) |
| Abstraction Boundary | [challenges/abstraction_boundary.py](challenges/abstraction_boundary.py) |

Run tests for this module:

```bash
pytest tests/02_model_strategy/ -v
```
