import pytest
from disemvowel_trolls import disemvowel
import random
import string

@pytest.mark.parametrize("inp, expected", [
    ("This website is for losers LOL!", "Ths wbst s fr lsrs LL!"),
    ("No offense but,\nYour writing is among the worst I've ever read", "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"),
    ("What are you, a communist?", "Wht r y,  cmmnst?"),
])
def test_fixed(inp, expected):
    assert disemvowel(inp) == expected

vowels = 'aeiouAEIOU'

def test_random():
    for _ in range(50):
        random_letters = ''.join(random.choices(string.ascii_letters + " .,!?'\n", k=30))
        expected = ''.join([c for c in random_letters if c not in vowels])
        assert disemvowel(random_letters) == expected
