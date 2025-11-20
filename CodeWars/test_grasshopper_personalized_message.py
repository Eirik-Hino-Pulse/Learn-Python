from grasshopper_personalized_message import grasshopper_personalized_message
import random

def test_basic_cases():
    print("\nFixed Tests")
    assert grasshopper_personalized_message('Daniel', 'Daniel') == 'Hello boss'
    assert grasshopper_personalized_message('Greg', 'Daniel') == 'Hello guest'

def test_random_cases():
    print("\nRandom Tests")
    names = ['Joe', 'Greg', 'Daniel', 'Bob']

    for _ in range(50):
        user = random.choice(names)
        boss = random.choice(names)
        expected = 'Hello boss' if user == boss else 'Hello guest'
        print(f"testing for greet({user!r}, {boss!r})")
        result = grasshopper_personalized_message(user, boss)
        assert result == expected, f"{result!r} should equal {expected!r}"