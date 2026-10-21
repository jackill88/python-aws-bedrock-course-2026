# Using Both

Most production paths use Lambda **and** ECS, for different units of work. One runtime for everything is how either the 29-second door or a always-on cluster becomes the architecture.

## Splits that hold up

| Path | Who does what |
|------|----------------|
| Admission then slow work | Lambda checks identity, tenant, and budget, then enqueues. An ECS worker calls Converse. The HTTP call returns a job id |
| Chat under the edge ceiling | Lambda or a small Fargate service, chosen by `choose_compute`, calls Retrieve and Converse itself |
| Agent with a dangerous tool | The agent loop calls a short Lambda action group for reads. Writes go return-of-control into Step Functions and, if the tool is slow, an ECS task |
| Nightly eval or backfill | Neither interactive runtime. Batch inference (Module 01), or a Fargate task that submits the batch job and exits |
| Human approval | Step Functions callback. The model call has already finished. Do not hold a Lambda open while a person decides |

Step Functions is the graph (Module 06). It is not a third place to host the model. Standard workflows can last much longer than Lambda; each state that calls Bedrock still runs inside a Lambda or an ECS task with that runtime's limits.

## Identity

| Principal | May |
|-----------|-----|
| Lambda execution role for the gateway | `Converse` and `Retrieve` on the pinned ARNs for that use case |
| Lambda execution role for one tool | That tool's API, and Bedrock only if the tool itself must call a model |
| ECS task role | Same narrow data-plane actions as the gateway it replaces |
| Agent resource role | `lambda:InvokeFunction` on the action-group function, not on every function in the account |
| Deploy role | Push an image or update a function. It does not need `bedrock:InvokeModel` |

A function URL or an ALB without your authorizer is a public Bedrock wallet. The authorizer is yours (IAM, JWT). Bedrock's IAM check is the second door, not the first.

## Failure you should be able to name

| Failure | What you configured wrong |
|---------|---------------------------|
| API returns 29-second timeout, Lambda log shows a later success | The edge ceiling was ignored. The user failed; the model may still have run |
| Duplicate refund after an async invoke error | `duplicate_side_effect` with no idempotency key |
| Two workers process one SQS message | Visibility timeout shorter than the Bedrock call |
| ECS tasks flap when Bedrock throttles | Health check depends on a successful model call |
| Private subnet cannot reach the runtime | No `bedrock-runtime` endpoint, or the security group does not allow it |
| Cold start blows the interactive SLO | Spiky Lambda was fine; this path is steady and needed provisioned concurrency or a min task count |

Review line: **"Pick the runtime per unit of work. The edge timeout and the retry policy are part of that pick."**
