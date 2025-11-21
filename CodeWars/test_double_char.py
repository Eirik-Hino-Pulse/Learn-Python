import pytest
from double_char import double_char
import random
import string

@pytest.mark.parametrize("s, expected", [
    ("String", "SSttrriinngg"),
    ("Hello World", "HHeelllloo  WWoorrlldd"),
    ("1234!_ ", "11223344!!__  "),
])
def test_fixed(s, expected):
    assert double_char(s) == expected

def test_random():
    for _ in range(10):
        s = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + " ", k=random.randint(5, 30)))
        expected = ''.join(ch*2 for ch in s)
        assert double_char(s) == expected
