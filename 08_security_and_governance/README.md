# Module 08: Security and Governance

Bedrock security is ordinary AWS security applied to a data plane that contains prompts. The lead-architect failures are broad IAM, public runtime paths for restricted data, invocation logs that become a second copy of the corpus, and residency reviews that forget inference-profile destinations.

## Learning Objectives

By the end of this module you will be able to:

- Allow or deny Bedrock actions from a small role matrix instead of `bedrock:*`
- Choose a public endpoint or an interface VPC endpoint from the data class
- Keep, restrict, or drop log fields
- Reject a region set that is empty or outside the allowed list

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | IAM Least Privilege | [theory/01_iam_least_privilege.md](theory/01_iam_least_privilege.md) |
| 2 | Private Network Paths | [theory/02_private_network_paths.md](theory/02_private_network_paths.md) |
| 3 | Encryption, Logging, and Residency | [theory/03_encryption_logging_residency.md](theory/03_encryption_logging_residency.md) |
| 4 | Multi-Account Governance | [theory/04_multi_account_governance.md](theory/04_multi_account_governance.md) |

## Quiz

Test your understanding: [quizzes/security_governance_quiz.md](quizzes/security_governance_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Authorize | [challenges/authorize.py](challenges/authorize.py) |
| Network Path | [challenges/network_path.py](challenges/network_path.py) |
| Log Field Policy | [challenges/log_field_policy.py](challenges/log_field_policy.py) |
| Residency Allowed | [challenges/residency_allowed.py](challenges/residency_allowed.py) |

Run tests for this module:

```bash
pytest tests/08_security_and_governance/ -v
```
