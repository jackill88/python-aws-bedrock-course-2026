# Module 12: Lambda and ECS

Bedrock hosts the model. Lambda and ECS host **your** code: the gateway, the action-group tool, the queue worker. This module is where that process runs, what timeout the edge actually enforces, and how an asynchronous retry becomes a second model call.

## Learning Objectives

By the end of this module you will be able to:

- Keep foundation-model inference on Bedrock, and choose Lambda or ECS/Fargate only for the caller
- Send stateless events and short response streams to Lambda, and held sessions or over-15-minute work to Fargate
- Name the platform timeout for API Gateway, a Lambda function URL, an ALB, and an ECS task
- Treat asynchronous Lambda retries as duplicate model calls, and as duplicate side effects when the tool writes

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Callers, Not Hosts | [theory/01_callers_not_hosts.md](theory/01_callers_not_hosts.md) |
| 2 | Lambda | [theory/02_lambda.md](theory/02_lambda.md) |
| 3 | ECS and Fargate | [theory/03_ecs_and_fargate.md](theory/03_ecs_and_fargate.md) |
| 4 | Using Both | [theory/04_using_both.md](theory/04_using_both.md) |

## Quiz

Test your understanding: [quizzes/lambda_and_ecs_quiz.md](quizzes/lambda_and_ecs_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Choose Compute | [challenges/choose_compute.py](challenges/choose_compute.py) |
| Platform Timeout | [challenges/platform_timeout_s.py](challenges/platform_timeout_s.py) |
| Async Duplicate Risk | [challenges/async_duplicate_risk.py](challenges/async_duplicate_risk.py) |

Run tests for this module:

```bash
pytest tests/12_lambda_and_ecs/ -v
```
