import pytest
from sum_mixed_array import sum_mix
import random

@pytest.mark.parametrize("arr, expected", [
    ([9, 3, '7', '3'], 22),
    (['5', '0', 9, 3, 2, 1, '9', 6, 7], 42),
    (['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'], 41),
    (['1', '5', '8', 8, 9, 9, 2, '3'], 45),
    ([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7], 61),
])
def test_fixed(arr, expected):
    assert sum_mix(arr) == expected

def test_random():
    for _ in range(10):
        arr = [random.choice([random.randint(-100, 100), str(random.randint(-100, 100))]) for _ in range(random.randint(5, 80))]
        expected = sum(int(x) for x in arr)
        assert sum_mix(arr) == expected
#pytest