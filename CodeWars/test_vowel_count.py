import pytest
from vowel_count import get_count
import random
import string

@pytest.mark.parametrize("sentence, expected", [
    ("aeiou", 5),
    ("y", 0),
    ("bcdfghjklmnpqrstvwxz y", 0),
    ("", 0),
    ("abracadabra", 5),
])
def test_fixed(sentence, expected):
    assert get_count(sentence) == expected

vowels = 'aeiou'
consonants = ''.join(sorted(set(string.ascii_lowercase) - set(vowels) - set('y')))

def test_random():
    for _ in range(100):
        count = random.randint(0, 10)
        sentence = ''.join(random.choices(vowels, k=count)) + ''.join(random.choices(consonants + ' ', k=10))
        expected = sum(1 for c in sentence if c in vowels)
        assert get_count(sentence) == expected
