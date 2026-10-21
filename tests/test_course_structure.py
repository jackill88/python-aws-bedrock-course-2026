"""The course tree matches what the navigator and the checklist expect."""

from pathlib import Path

from course_nav.course_loader import discover_modules

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    "01_bedrock_platform",
    "02_model_strategy",
    "03_inference_architecture",
    "04_prompt_systems",
    "05_rag_architecture",
    "06_agents_and_orchestration",
    "07_guardrails_and_safety",
    "08_security_and_governance",
    "09_reliability_cost_and_ops",
    "10_evaluation_and_release",
    "11_system_design",
    "12_lambda_and_ecs",
    "13_summary",
]


def test_module_order() -> None:
    modules = discover_modules(ROOT)
    assert [m.module_id for m in modules] == EXPECTED


def test_each_module_has_lessons_and_a_quiz() -> None:
    for module in discover_modules(ROOT):
        assert module.readme is not None
        assert len(module.theory) >= 3
        assert len(module.quizzes) >= 1


def test_coding_modules_have_challenges_and_tests() -> None:
    for module in discover_modules(ROOT):
        if module.module_id == "13_summary":
            assert module.challenges == []
            continue
        assert module.challenges, module.module_id
        for challenge in module.challenges:
            test_file = ROOT / "tests" / module.module_id / f"test_{challenge.path.stem}.py"
            assert test_file.is_file(), test_file
