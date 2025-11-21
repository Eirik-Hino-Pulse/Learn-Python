import pytest
from feast_of_many_beasts import feast
import random
import string

@pytest.mark.parametrize("beast, dish, expected", [
    ("great blue heron", "garlic naan", True),
    ("chickadee", "chocolate cake", True),
    ("brown bear", "bear claw", False),
    ("lion", "lemon tart", False),
    ("giraffe", "grape eclair", True),
    ("zebra", "zebra cake", True),
])
def test_fixed(beast, dish, expected):
    assert feast(beast, dish) == expected

def random_word(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def test_random():
    for _ in range(10):
        # Construct beasts and dishes that should match
        first = random.choice(string.ascii_lowercase)
        last = random.choice(string.ascii_lowercase)
        beast = first + random_word(random.randint(2, 8)) + last
        dish = first + random_word(random.randint(2, 8)) + last
        assert feast(beast, dish) == True
        # And non-matching
        dish2 = random_word(random.randint(3, 10))
        if dish2[0] != beast[0] or dish2[-1] != beast[-1]:
            assert feast(beast, dish2) == False
