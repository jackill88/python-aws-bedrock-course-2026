import pytest

from shared.testing import load_challenge

case_pattern = load_challenge(
    "11_system_design", "case_pattern.py"
).case_pattern


def test_cases() -> None:
    assert case_pattern("hr_policy_qa") == "managed_kb_rag"
    assert case_pattern("claims_adjudication") == "workflow_human_approval"
    assert case_pattern("it_ops_remediation") == "hybrid_agent_read_default"
    assert case_pattern("multi_team_platform") == "shared_platform_per_app_guardrails"


def test_unknown() -> None:
    with pytest.raises(ValueError):
        case_pattern("chatbot")
