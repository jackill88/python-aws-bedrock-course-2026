import pytest

from shared.testing import load_challenge

data_handling_owner = load_challenge(
    "01_bedrock_platform", "data_handling_owner.py"
).data_handling_owner


@pytest.mark.parametrize(
    ("topic", "owner"),
    [
        ("base_model_training_on_customer_prompts", "aws_does_not"),
        ("model_hosting_availability", "aws"),
        ("patching_foundation_model_runtime", "aws"),
        ("iam_who_can_invoke", "customer"),
        ("prompt_content_policy", "customer"),
        ("vpc_endpoint_adoption", "customer"),
        ("encryption_in_transit", "shared"),
    ],
)
def test_owners(topic: str, owner: str) -> None:
    assert data_handling_owner(topic) == owner


def test_unknown_topic() -> None:
    with pytest.raises(ValueError):
        data_handling_owner("fine_print_we_did_not_review")
