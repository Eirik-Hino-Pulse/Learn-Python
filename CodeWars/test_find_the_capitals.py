import pytest
from find_the_capitals import capitals
import random
import string

@pytest.mark.parametrize("inp, expected", [
    ("CodEWaRs", [0,3,4,6]),
    ("HelloWorld", [0,5]),
    ("ABCdef", [0,1,2]),
    ("python", []),
    ("XxYyZz", [0,2,4]),
    ("", [])
])
def test_fixed(inp, expected):
    assert capitals(inp) == expected

def test_random():
    for _ in range(30):
        n = random.randint(5, 20)
        chars = [random.choice([c.lower(), c.upper()]) for c in random.choices(string.ascii_uppercase, k=n)]
        word = ''.join(chars)
        expected = [i for i, c in enumerate(word) if c.isupper()]
        assert capitals(word) == expected
