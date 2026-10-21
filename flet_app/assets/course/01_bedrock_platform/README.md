# Module 01: Bedrock Platform

Place Amazon Bedrock in the architecture before you pick a model. This module is the control-plane / data-plane split, how you pay for inference, and which risks sit with AWS versus the owning team.

## Learning Objectives

By the end of this module you will be able to:

- Separate Bedrock management APIs from runtime inference APIs
- Choose on-demand, provisioned throughput, or batch from workload shape
- State the shared-responsibility line for prompts, IAM, hosting, and training use
- Reject a design that treats "the model" as the system

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Platform Mental Model | [theory/01_platform_mental_model.md](theory/01_platform_mental_model.md) |
| 2 | Control Plane and Data Plane | [theory/02_control_plane_and_data_plane.md](theory/02_control_plane_and_data_plane.md) |
| 3 | Consumption and Commercial Model | [theory/03_consumption_and_commercial_model.md](theory/03_consumption_and_commercial_model.md) |
| 4 | Responsibility and Placement | [theory/04_responsibility_and_placement.md](theory/04_responsibility_and_placement.md) |

## Quiz

Test your understanding: [quizzes/bedrock_platform_quiz.md](quizzes/bedrock_platform_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Classify API Plane | [challenges/classify_api_plane.py](challenges/classify_api_plane.py) |
| Choose Consumption Mode | [challenges/choose_consumption_mode.py](challenges/choose_consumption_mode.py) |
| Data Handling Owner | [challenges/data_handling_owner.py](challenges/data_handling_owner.py) |

Run tests for this module:

```bash
pytest tests/01_bedrock_platform/ -v
```
