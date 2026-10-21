# Module 09: Reliability, Cost, and Operations

A Bedrock system is up when it answers inside the latency budget **and** the answer still meets the quality bar. HTTP 200 with an ungrounded paragraph is a breach. So is a provisioned model you pay for and do not allocate.

## Learning Objectives

By the end of this module you will be able to:

- Separate availability, quality, and latency breaches
- Pick batch, on-demand, provisioned, or provisioned-plus-burst from the traffic shape
- Price a request from split token meters without double-counting cache tokens
- Name the signals an incident needs that are not CPU

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | SLIs That Include Quality | [theory/01_slis_that_include_quality.md](theory/01_slis_that_include_quality.md) |
| 2 | Capacity, Quotas, and Throughput | [theory/02_capacity_quotas_throughput.md](theory/02_capacity_quotas_throughput.md) |
| 3 | Cost Architecture | [theory/03_cost_architecture.md](theory/03_cost_architecture.md) |
| 4 | Observability and Incidents | [theory/04_observability_and_incidents.md](theory/04_observability_and_incidents.md) |

## Quiz

Test your understanding: [quizzes/reliability_cost_ops_quiz.md](quizzes/reliability_cost_ops_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| SLO Status | [challenges/slo_status.py](challenges/slo_status.py) |
| Capacity Plan | [challenges/capacity_plan.py](challenges/capacity_plan.py) |
| Token Cost | [challenges/token_cost_usd.py](challenges/token_cost_usd.py) |

Run tests for this module:

```bash
pytest tests/09_reliability_cost_and_ops/ -v
```
