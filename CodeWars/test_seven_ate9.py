import pytest
from seven_ate9 import seven_ate9
import re
from random import randint

@pytest.mark.parametrize("s, expected", [
    ('165561786121789797', '16556178612178977'),
    ('797', '77'),
    ('7979797', '7777'),
    ('16797', '1677'),
    ('77', '77'),
    ('7927', '7927'),
    ('1779', '1779'),
    ('a779', 'a779'),
    ('17797a', '1777a'),
    ('797 9 7','77 9 7'),
])
def test_fixed(s, expected):
    assert seven_ate9(s) == expected

def test_random():
    base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    def sol_ate9(s):
        d = s
        while '797' in d:
            d = re.sub(r'797', '77', d)
        return d
    for _ in range(40):
        s = [base[randint(0,9)]]
        for i in range(randint(1,15)):
            if s[-1] == '7':
                while randint(0,1)==1: s += ['9','7']
            if randint(0,9) > 8: s += ['7','9','7']
            else: s += [base[randint(0,9)]]
        s = "".join(s)
        assert seven_ate9(s) == sol_ate9(s)
