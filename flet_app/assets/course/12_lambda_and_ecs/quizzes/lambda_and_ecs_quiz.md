# Lambda And ECS Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** Lambda and ECS, in this course, are:

- A) Where the foundation model is hosted
- B) Where your caller runs. Bedrock still hosts the model
- C) Replacements for guardrails
- D) Required only when you fine-tune

**2.** A stateless event whose worst case is 30 seconds maps to:

- A) `ecs_fargate`
- B) `lambda`
- C) EC2 GPU workers
- D) Batch inference only

**3.** A WebSocket session pinned to the process maps to:

- A) `lambda`, because each turn is short
- B) `ecs_fargate`
- C) `api_gateway` as the compute result
- D) Provisioned throughput with no compute

**4.** A job whose worst case is 901 seconds maps to:

- A) `lambda` with a 901-second timeout
- B) `ecs_fargate`
- C) `lambda` if the pattern is `event`
- D) API Gateway, which extends the limit

**5.** `platform_timeout_s("api_gateway")` is:

- A) 900
- B) 29
- C) 4000
- D) `None`

**6.** `platform_timeout_s("ecs_task")` is:

- A) 900
- B) 29
- C) `None`. You still set an application deadline
- D) 60, and it cannot be changed

**7.** An ALB in front of a long Bedrock stream:

- A) Defaults to an idle timeout that can cut the stream unless you raise it
- B) Has the same 29-second cap as API Gateway
- C) Removes the need for a task role
- D) Hosts the foundation model

**8.** Asynchronous Lambda invoke of a write tool is:

- A) `client_retries_only`
- B) `duplicate_side_effect`
- C) Safe because Bedrock dedupes tools
- D) `duplicate_model_call` only, with no side-effect concern

**9.** A synchronous Lambda read is:

- A) `duplicate_side_effect`
- B) `client_retries_only`
- C) Free of any caller retry
- D) `ecs_fargate`

**10.** A design that uses both runtimes well is:

- A) Lambda for admission and enqueue, ECS for the slow Converse worker
- B) EC2 GPUs for the model and Lambda for IAM
- C) One Lambda held open during human approval
- D) API Gateway in front of a 2-minute generation with no other edge

## Answers

1. B  2. B  3. B  4. B  5. B  6. C  7. A  8. B  9. B  10. A
