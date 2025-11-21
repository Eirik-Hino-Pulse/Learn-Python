import pytest
from quarter_of import quarter_of
import random

@pytest.mark.parametrize("month, expected", [
    (3, 1),
    (8, 3),
    (11, 4),
    (1, 1),
    (6, 2),
    (12, 4),
])
def test_fixed(month, expected):
    assert quarter_of(month) == expected

def test_random():
    for _ in range(10):
        month = random.randint(1, 12)
        # quarter calculation for test (not for your solution!)
        expected = (month - 1) // 3 + 1
        assert quarter_of(month) == expected
