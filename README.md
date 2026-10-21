# AWS Bedrock — Lead Architect Course

A self-paced course for people who already build on AWS and need to make **lead-architect** decisions about Amazon Bedrock: model strategy, retrieval, agents, guardrails, security, cost, evaluation, and design review.

The exercises do not call AWS. They encode the decisions a review should be able to defend. Optional live labs are listed separately and need an account.

## Learning Objectives

After finishing this course, you will be able to:

- Place Bedrock against SageMaker or self-hosted inference, and separate the control plane from the data plane
- Choose on-demand, provisioned throughput, or batch from latency and traffic shape
- Pin a model tier, a fallback, and a versioned prompt behind a gateway
- Budget tokens, cache only stable prefixes, and retry only when the call is safe to repeat
- Decide among prompt-only, long context, RAG, and fine-tuning — then isolate tenants outside the model
- Keep write tools in workflows with idempotency and human approval
- Apply guardrails, PII actions, and grounding checks without pretending they replace IAM
- Constrain roles, private network paths, log fields, and processing regions
- Define SLOs that include groundedness, and block releases that fail safety, shadow quality, or unjustified cost
- Place the caller on Lambda or on ECS/Fargate, and respect edge timeouts and asynchronous retries

## Course Structure

| Module | Topic | Challenges |
|--------|-------|------------|
| [01_bedrock_platform](01_bedrock_platform/README.md) | Bedrock Platform | 3 |
| [02_model_strategy](02_model_strategy/README.md) | Model Strategy | 3 |
| [03_inference_architecture](03_inference_architecture/README.md) | Inference Architecture | 3 |
| [04_prompt_systems](04_prompt_systems/README.md) | Prompt Systems | 3 |
| [05_rag_architecture](05_rag_architecture/README.md) | RAG Architecture | 4 |
| [06_agents_and_orchestration](06_agents_and_orchestration/README.md) | Agents and Orchestration | 3 |
| [07_guardrails_and_safety](07_guardrails_and_safety/README.md) | Guardrails and Safety | 3 |
| [08_security_and_governance](08_security_and_governance/README.md) | Security and Governance | 4 |
| [09_reliability_cost_and_ops](09_reliability_cost_and_ops/README.md) | Reliability, Cost, and Operations | 3 |
| [10_evaluation_and_release](10_evaluation_and_release/README.md) | Evaluation and Release | 3 |
| [11_system_design](11_system_design/README.md) | System Design | 3 |
| [12_lambda_and_ecs](12_lambda_and_ecs/README.md) | Lambda and ECS | 3 |
| [13_summary](13_summary/README.md) | Summary | — |

Each module contains:

- **`theory/`** — Lessons with decision tables and the code the challenges expect
- **`quizzes/`** — Self-check multiple-choice quizzes, answers at the bottom
- **`challenges/`** — Function stubs for you to implement

Tests live in **`tests/`**, one file per challenge, plus `tests/test_course_structure.py` which checks that the tree is intact.

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Study a module

Open the module `README.md`, read the theory lessons in order, then implement the challenges. The docstring is the contract. The lesson shows the same rules in context.

### 3. Implement challenges

Each challenge file contains a function that still says `pass`. Replace that with your solution.

```bash
pytest tests/01_bedrock_platform/test_classify_api_plane.py -v
pytest tests/01_bedrock_platform/ -v
```

### 4. Track completion

```bash
pytest -v
```

`tests/test_course_structure.py` passes immediately. Challenge tests pass when your implementations match the contracts. When **all** tests pass, you have finished the coding half of the course. Module 13's checklist is the other half.

Prices, quotas, and minimum cache sizes move. Lessons say so when a number is a teaching threshold rather than a vendor constant. Confirm the live price card and service quotas before you take a number from this course into a budget meeting.

## Course Navigator App

A Streamlit GUI browses the lessons, tracks module progress in SQLite, and points at the challenge files.

```bash
pip install -r requirements-app.txt
streamlit run app/main.py
```

Progress is stored in `data/progress.db` (created on first launch). Mark modules complete as you finish each section.

### Android app (Flet, offline, theory only)

The Android navigator mirrors the Streamlit UI and skips the coding challenges — theory, quizzes, and progress only.

```bash
pip install -r requirements-flet.txt

# Development (uses this repo's lessons directly)
flet run flet_app/main.py

# Build an APK (bundle markdown first)
python flet_app/prepare_assets.py
flet build apk
```

The APK is written to `build/apk/`. Progress on a device uses the app's private storage and the same SQLite schema as the desktop app.

Requires the [Android SDK](https://developer.android.com/studio). Run `flet doctor` if the build fails.

## Project Layout

```
.
├── README.md
├── requirements.txt
├── pytest.ini
├── 01_bedrock_platform/
│   ├── README.md
│   ├── theory/
│   ├── quizzes/
│   └── challenges/
├── ...
├── 12_lambda_and_ecs/
├── 13_summary/
├── tests/
├── app/                     # Streamlit course navigator
├── course_nav/              # Shared discovery + SQLite progress
├── flet_app/                # Offline Android navigator (theory + quizzes)
├── labs/                    # Optional live AWS exercises
└── data/                    # progress.db (created by the app)
```

## How Challenges Work

Implement the function in each challenge file. Signatures and docstrings are the spec. Tests load the file by path, so you do not package anything.

No AWS credentials, no network, and no foundation-model call are required.

## Tech Stack

| Layer | Choice |
|-------|--------|
| Language | Python ≥ 3.10 |
| Testing | pytest |
| Desktop GUI | Streamlit (optional) |
| Mobile GUI | Flet (optional) |
| Progress | SQLite |

## Tips

1. Read the lesson before you fill in the stub. The tables are the design, not decoration.
2. Say the isolation class, the tool's side effect, and the processing regions out loud before you pick a service.
3. Run one test file while you iterate. Run the full suite before you mark a module complete.
4. Use the quiz before you move on. The answers are at the bottom on purpose — try the questions first.
5. For the system-design module, practice the latency split and the case pattern until you do not need the table.

## License

Personal learning use. Adapt and extend as you like.
