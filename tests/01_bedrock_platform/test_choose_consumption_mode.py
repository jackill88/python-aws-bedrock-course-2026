import pytest

from shared.testing import load_challenge

choose_consumption_mode = load_challenge(
    "01_bedrock_platform", "choose_consumption_mode.py"
).choose_consumption_mode


def test_batch_when_async_and_not_interactive() -> None:
    assert (
        choose_consumption_mode(1_000_000, False, True, True) == "batch"
    )


def test_interactive_async_flag_does_not_select_batch() -> None:
    assert choose_consumption_mode(500, True, False, True) == "on_demand"


def test_provisioned_for_steady_high_volume() -> None:
    assert (
        choose_consumption_mode(100_000, True, True, False) == "provisioned"
    )


def test_low_volume_steady_stays_on_demand() -> None:
    assert choose_consumption_mode(99_999, True, True, False) == "on_demand"


def test_spiky_high_volume_stays_on_demand() -> None:
    assert choose_consumption_mode(250_000, True, False, False) == "on_demand"


def test_negative_volume() -> None:
    with pytest.raises(ValueError):
        choose_consumption_mode(-1, False, False, True)
