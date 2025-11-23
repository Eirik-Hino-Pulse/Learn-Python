import pytest
from divide_and_conquer import div_con

@pytest.mark.parametrize("x, expected", [
    ([9, 3, '7', '3'], 2),
    (["5", "0", 9, 3, 2, 1, "9", 6, 7], 14),
    (["3", 6, 6, 0, "5", 8, 5, "6", 2,'0'], 13),
    (["1", "5", "8", 8, 9, 9, 2, "3"], 11),
    ([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7], 61),
    ([1, '1', 2, '2', 3, '3'], 0),
    (["0", 0], 0),
    (["0"], 0),
    ([0], 0)
])
def test_fixed(x, expected):
    assert div_con(x) == expected

import random

def test_random():
    for _ in range(30):
        nums = [random.randint(-100, 100) for _ in range(random.randint(2, 10))]
        strs = [str(random.randint(-100, 100)) for _ in range(random.randint(2, 10))]
        arr = nums + strs
        random.shuffle(arr)
        expected = sum(n for n in arr if isinstance(n, int)) - sum(int(s) for s in arr if isinstance(s, str))
        assert div_con(arr) == expected
