# Responsibility and Placement

Bedrock removes the undifferentiated work of **hosting** a foundation model. It does not remove accountability for **what the system does** with customer data. Architecture reviews fail when that line is fuzzy.

## The line

| Topic | Owner | Meaning |
|-------|-------|---------|
| Base-model training on your prompts | AWS does not use Bedrock customer inputs to train the base models | Still confirm Marketplace and any feature that says otherwise |
| Patching and availability of the model runtime | AWS | You design for timeout, throttle, and regional failure |
| Who may invoke a model | Customer | IAM, SCPs, your gateway |
| What the prompt is allowed to ask | Customer | Product policy, guardrails, human process |
| Encryption in transit | Shared | AWS provides TLS on the API; you choose private connectivity and how clients reach you |
| Adopting a VPC interface endpoint | Customer | The endpoint exists; you create it, route to it, and lock down the public path |
| Content of retrieved documents | Customer | Bedrock does not know your tenancy rules |

Review line: **"No training on our prompts is a Bedrock property. Least privilege is ours."**

`data_handling_owner` encodes that table:

| Topic key | Return |
|-----------|--------|
| `base_model_training_on_customer_prompts` | `aws_does_not` |
| `model_hosting_availability` | `aws` |
| `patching_foundation_model_runtime` | `aws` |
| `iam_who_can_invoke` | `customer` |
| `prompt_content_policy` | `customer` |
| `vpc_endpoint_adoption` | `customer` |
| `encryption_in_transit` | `shared` |

Any other topic raises `ValueError`. Do not collapse "AWS does not train on prompts" into a generic `aws` bucket. It is a specific negative commitment, and Marketplace models need a second look at their own terms.

## Placement checklist before you commit

| Question | If the answer is yes |
|----------|----------------------|
| Do we need a model Bedrock does not offer in the residency region? | SageMaker or another host, or change the residency design |
| Is this mostly API inference with AWS IAM? | Bedrock stays the default |
| Do we need custom weights as the core product? | Customization on Bedrock where supported, else SageMaker |
| Will a third-party Marketplace model see regulated text? | Legal review of that model's terms before IAM allows it |
| Can prompts leave the region via an inference profile? | Either pin a regional model or expand the allowed region list on purpose |

## Account shape

A lead-architect default for a company with more than one product:

| Account | Holds |
|---------|-------|
| Platform | Guardrail baselines, model allow-list, provisioned throughput, logging configuration, SCPs |
| Application (per domain) | Runtime roles, knowledge-base data, product prompts |
| Logging / audit | Invocation logs and CloudTrail, restricted read for auditors |
| Sandbox | On-demand only, no production data, tight spend cap |

Production data does not go to the sandbox "just to try a prompt." That shortcut is how regulated text lands in a personal account.

## What you document in the ADR

One page is enough:

1. Why Bedrock, not SageMaker or self-host, for **this** use case
2. Model class and whether the id is pinned or routed
3. Regions that may process data
4. Consumption mode and the volume assumption behind it
5. What is logged, for how long, and who can read it
6. The runtime role's allowed actions (they should fit on a short list)

If any of the six is "TBD at launch," the design is not ready for production traffic.
