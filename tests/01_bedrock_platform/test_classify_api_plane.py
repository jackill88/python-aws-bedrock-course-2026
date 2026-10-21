import pytest

from shared.testing import load_challenge

classify_api_plane = load_challenge(
    "01_bedrock_platform", "classify_api_plane.py"
).classify_api_plane


@pytest.mark.parametrize(
    "api_name",
    [
        "CreateGuardrail",
        "CreateKnowledgeBase",
        "PutModelInvocationLoggingConfiguration",
        "CreateProvisionedModelThroughput",
        "ListFoundationModels",
    ],
)
def test_control_plane(api_name: str) -> None:
    assert classify_api_plane(api_name) == "control"


@pytest.mark.parametrize(
    "api_name",
    [
        "Converse",
        "ConverseStream",
        "InvokeModel",
        "Retrieve",
        "RetrieveAndGenerate",
        "ApplyGuardrail",
    ],
)
def test_data_plane(api_name: str) -> None:
    assert classify_api_plane(api_name) == "data"


def test_unknown_api() -> None:
    with pytest.raises(ValueError):
        classify_api_plane("DeleteBucket")
