import pytest
from convert_array_of_strings_to_numbers import to_float_array

@pytest.mark.parametrize("input_arr, expected", [
    (["1", "2", "3"], [1.0, 2.0, 3.0]),
    (["1.1", "2.2", "3.3"], [1.1, 2.2, 3.3]),
    (["0", "-1", "4.5"], [0.0, -1.0, 4.5]),
    (["100"], [100.0]),
    (["0.0", "00.00"], [0.0, 0.0]),
    ([], []),
])
def test_fixed(input_arr, expected):
    assert to_float_array(input_arr) == expected

import random

def test_random():
    for _ in range(20):
        n = random.randint(1, 10)
        floats = [random.uniform(-1000, 1000) for _ in range(n)]
        input_arr = [str(f) for f in floats]
        expected = [float(x) for x in input_arr]
        assert to_float_array(input_arr) == expected
