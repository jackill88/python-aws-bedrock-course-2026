# The Evaluation Pyramid

Bedrock model evaluation can run automatic and human jobs against a dataset you supply. That is one shelf of the pyramid. A platform still needs a frozen set in CI, a shadow comparison, and a production sample. Skipping to "we'll watch thumbs-down" means the first measurement is the incident.

## Layers

| Layer | Question | Cadence |
|-------|----------|---------|
| Unit checks | Schema valid, tenant filter present, guardrail version pinned | Every commit |
| Offline set | Does this prompt and model beat the frozen cases? | Every candidate |
| Shadow | On real traffic, is the candidate worse than what users see? | Before promotion |
| Online sample | Did production drift after launch? | Continuously, small |
| Human audit | Are the automatic labels still honest? | Scheduled, and after every judge change |

The offline set is versioned. If you edit a case to make the new prompt pass, you changed the exam. Record that as a set change with a reason, not as a quiet score improvement.

## What goes in the set

| Include | Exclude |
|---------|---------|
| Real failure classes: stale policy, wrong tenant temptation, tool-argument injection, empty retrieval | Only the demo questions from the kickoff |
| Expected citations or expected abstain | A single "golden paragraph" that rejects every valid paraphrase |
| Cases per important tenant type and language | Production secrets and live customer payloads in the repo |

Synthetic cases are allowed when they encode a policy. They are not a substitute for a sample of real questions once you have traffic. Scrub that sample before it lands in an eval bucket the whole company can read.

Review line: **"The set is a product artifact. Changing it is a review, not a notebook convenience."**

Bedrock's evaluation jobs are a useful runner for model-versus-model comparisons. The gate in this module does not care which runner produced the score. It cares that the score is on the frozen set and that safety is a separate boolean.
