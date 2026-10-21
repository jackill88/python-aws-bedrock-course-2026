# Regulated Workflow and Operations Agent

Two cases get conflated because both "use AI." One decides about a person or a claim. The other restarts a server. The patterns differ.

## Claims and other regulated decisions

`case_pattern("claims_adjudication")` returns `workflow_human_approval`.

The model may extract fields, retrieve policy, and draft a recommendation. It does not commit the decision. A workflow holds the case, a person approves the bound arguments, and the system of record stores the outcome plus the model id, prompt version, passage ids, and approver. That pack is the audit file.

| Do | Do not |
|----|--------|
| Pin model and prompt. Changes are releases | Let an agent loop "finish the claim" |
| Account or strong isolation as the data class requires | A shared index because the vendor demo was single-tenant |
| Abstain when passages are missing | A fluent denial with no citation |
| Human approval on the irreversible write | A chat sentence that says the user agreed |

Residency includes every inference-profile destination. If the allowed list cannot hold them, pin a regional model and accept the quota work.

## IT operations

`case_pattern("it_ops_remediation")` returns `hybrid_agent_read_default`.

The agent may read tickets, metrics, and runbooks and propose a step. Restarts, security-group changes, and data deletion are writes or irreversible actions: they leave the agent and enter a workflow, with approval when Module 06 says so. Default tools are read. Write tools are explicit, idempotent, and off until the workflow calls them.

A pure agent with the production AWS role attached is the failure mode of this case. The review rejects it even if the demo was impressive.

Review line: **"Read tools can live in the loop. The production change lives in a workflow with a name."**
