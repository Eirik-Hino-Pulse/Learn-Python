from remove_exclamation_marks import remove_exclamation_marks
import random
import string

def test_fixed():
    print("\nFixed Tests")
    assert remove_exclamation_marks("Hello World!") == "Hello World"
    assert remove_exclamation_marks("Hello World!!!") == "Hello World"
    assert remove_exclamation_marks("Hi! Hello!") == "Hi Hello"
    assert remove_exclamation_marks("") == ""
    assert remove_exclamation_marks("Oh, no!!!") == "Oh, no"

def test_random():
    print("\nRandom Tests")
    letters = string.ascii_letters + ' '
    for _ in range(30):
        # Generate a random string with exclamation marks
        s = ''.join(random.choice(letters + "!"*3) for _ in range(random.randint(5, 40)))
        expected = s.replace("!", "")
        print(f"Testing for remove_exclamation_marks({s!r})")
        result = remove_exclamation_marks(s)
        assert result == expected, f"{result!r} should equal {expected!r}"