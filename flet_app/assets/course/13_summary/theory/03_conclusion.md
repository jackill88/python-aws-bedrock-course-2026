# Conclusion

Lead-architect Bedrock work is mostly refusal: refuse the shared key, the unfiltered index, the agent that can pay an invoice, the prompt edited in the console, the success metric that is only HTTP 200, the region list you did not write down.

The platform will keep adding models, routing features, and agent styles. The decisions in this course stay useful because they are about **data, authority, money, and evidence**. A new model id is a config change behind the gate. A new tool that writes is a workflow change. A new region on a profile is a residency change. None of those are "just try it in production."

## You are done when

- `pytest` is green for modules 01–12
- You can take an empty whiteboard and fill the checklist in Module 13 without the table in front of you
- You can point at a system you actually run and name the pin, the role, the isolation class, and the quality SLO

Optional live practice sits in [labs/README.md](../../labs/README.md). It needs an AWS account. It is not required for the tests, and it is not a substitute for them.

When a design review gets loud, return to one sentence from Module 01: Bedrock hosts the model call. You still own the product behavior.
