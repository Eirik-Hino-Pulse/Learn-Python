import pytest
from set_alarm import set_alarm
import random



@pytest.mark.parametrize("employed, vacation, expected", [
    (True, True, False),
    (True, False, True),
    (False, True, False),
    (False, False, False),
])
def test_fixed(employed, vacation, expected):
    assert set_alarm(employed, vacation) == expected

    for _ in range(100):
        employed = random.choice([True, False])
        vacation = random.choice([True, False])
        expected = employed and not vacation
        assert set_alarm(employed, vacation) == expected
