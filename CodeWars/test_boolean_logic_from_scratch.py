import pytest
from boolean_logic_from_scratch import func_or, func_xor

@pytest.mark.parametrize("a, b, or_expected, xor_expected", [
    (True, True, True, False),
    (True, False, True, True),
    (False, False, False, False),
    (0, 11, True, True),
    (None, [], False, False),
])
def test_fixed(a, b, or_expected, xor_expected):
    assert func_or(a, b) == or_expected
    assert func_xor(a, b) == xor_expected
