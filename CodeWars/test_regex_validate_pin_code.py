import pytest
from regex_validate_pin_code import validate_pin
import random
import string

@pytest.mark.parametrize("pin, expected", [
    ("1", False),
    ("12", False),
    ("123", False),
    ("12345", False),
    ("1234567", False),
    ("-1234", False),
    ("-12345", False),
    ("1.234", False),
    ("00000000", False),
    ("a234", False),
    (".234", False),
    ("1234", True),
    ("0000", True),
    ("1111", True),
    ("123456", True),
    ("098765", True),
    ("000000", True),
    ("123456", True),
    ("090909", True),
])
def test_fixed(pin, expected):
    assert validate_pin(pin) is expected

def test_random():
    # random invalid lengths
    for _ in range(20):
        length = random.choice([1, 2, 3, 5, 7, 8, 9, 10])
        pin = ''.join(random.choices(string.digits, k=length))
        assert validate_pin(pin) is False
    # random valid pins (4 or 6 digits, only digits)
    for _ in range(20):
        length = random.choice([4, 6])
        pin = ''.join(random.choices(string.digits, k=length))
        assert validate_pin(pin) is True
    # pins with wrong chars
    for _ in range(20):
        length = random.choice([4, 6])
        valid = ''.join(random.choices(string.digits, k=length))
        pos = random.randint(0, length-1)
        pin = valid[:pos] + random.choice(string.ascii_letters + '.-') + valid[pos+1:]
        assert validate_pin(pin) is False
