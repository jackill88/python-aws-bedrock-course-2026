from shared.testing import load_challenge

required_fields_present = load_challenge(
    "04_prompt_systems", "required_fields_present.py"
).required_fields_present


def test_empty_requirements_pass() -> None:
    assert required_fields_present({}, []) is True


def test_present_values_pass() -> None:
    assert required_fields_present({"order_id": "A1", "note": ""}, ["order_id"]) is True


def test_missing_and_none_fail() -> None:
    assert required_fields_present({"order_id": "A1"}, ["tenant_id"]) is False
    assert required_fields_present({"order_id": None}, ["order_id"]) is False


def test_extra_keys_are_allowed() -> None:
    payload = {"order_id": "A1", "debug": True}
    assert required_fields_present(payload, ["order_id"]) is True
