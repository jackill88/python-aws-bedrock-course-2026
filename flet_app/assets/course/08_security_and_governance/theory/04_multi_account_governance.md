# Multi-Account Governance

One account with production, sandbox, and logs is how a notebook ends up holding production prompts. Split them, and make the platform account the place where guardrail baselines and model allow-lists are born.

## A shape that scales past one team

| Account | Runs | Must not hold |
|---------|------|----------------|
| Org / security | SCPs, CloudTrail organization trail, key admins | Application prompts |
| Platform | Baseline guardrails, provisioned throughput, approved model ids, CI that promotes prompt versions | A product team's raw corpus as a convenience copy |
| Each product domain | Runtime, knowledge-base data, product prompts | The right to subscribe to arbitrary Marketplace models |
| Log archive | Invocation logs that passed the field policy, object-lock if audit asked for it | Interactive developer roles |
| Sandbox | On-demand, spend cap, synthetic data | Production snapshots "temporarily" |

Identity comes from your IdP into IAM Identity Center, then into roles. People do not share the `app_runtime` access key. The runtime is a role the service assumes.

## Cross-account

If a product account must invoke a model using a platform-owned guardrail or profile, prefer a narrow role in the product account allowed to call the specific ARNs, plus a resource-based policy where Bedrock supports it for that resource type. Do not build a transit role that can `AssumeRole` into platform admin. Test the confused-deputy case: a product role should not get to pass an arbitrary knowledge-base id the platform did not list.

## Change management

| Change | Path |
|--------|------|
| New model id | Platform allow-list, SCP check, eval, then the product config |
| Guardrail version | Promotion pipeline (Module 04 and 07) |
| Provisioned throughput purchase | Platform only, with a cost owner |
| Log field added | Security review. Default is not `keep` |

Review line: **"Sandbox can be loose on models and strict on data. Production is the opposite."**

Marketplace models are a governance event: different terms, sometimes different data handling, often a subscription outside the usual IAM change. Block them at the SCP in production accounts until legal and security have a ticket, not until a developer clicks Subscribe.
