# Shared Platform Blueprint

Several product teams will each want a model key. The lead-architect move is a platform, not a shared access key in a wiki.

`case_pattern("multi_team_platform")` returns `shared_platform_per_app_guardrails`.

## What the platform owns

| Platform | Each application |
|----------|------------------|
| Model allow-list and region list | The use case and the prompt artifact |
| Account layout, SCP backstops, VPC endpoint patterns | Its corpus and its tenancy class |
| Baseline guardrail and the rule that apps add stricter ones, not weaker ones, unless a waiver expires | Product-specific denied topics |
| Gateway: authn, tenant, budgets, pins, trace id | Tool implementations and approvals |
| Eval runner and the release gate | The offline set for that product |
| Provisioned capacity and showback | The decision to pay for a tier |
| Sandbox with synthetic data | Not a copy of production prompts |

Applications do not receive a long-lived key that can call `Converse` on any model. They receive a gateway use-case name. The platform maps that name to a model id, a guardrail version, and a token ceiling.

## What you refuse

| Request | Response |
|---------|----------|
| "Just the API key" | Gateway use-case, or a sandbox key with a spend cap and no production data |
| "We'll log prompts in our app logs" | Field policy. Metadata in their account, raw text only in the restricted store |
| "Our agent needs AdministratorAccess to be useful" | Read tools in the agent, writes in a role per tool |
| "Skip eval, it's internal" | Internal users still get a set. It can be smaller. It cannot be empty |

## Case map

`case_pattern` is the index for this module:

| Case | Pattern |
|------|---------|
| `hr_policy_qa` | `managed_kb_rag` |
| `claims_adjudication` | `workflow_human_approval` |
| `it_ops_remediation` | `hybrid_agent_read_default` |
| `multi_team_platform` | `shared_platform_per_app_guardrails` |

Unknown cases raise `ValueError`. A new case is a new review, not a default of "agent."

Review line: **"Teams ship use cases onto the platform. They do not ship new ways to call the runtime."**
