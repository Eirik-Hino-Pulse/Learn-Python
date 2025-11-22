"""
Instructions:
Trolls are attacking your comment section!
Remove all vowels from the input string (y is not a vowel).
For example: 'This website is for losers LOL!' -> 'Ths wbst s fr lsrs LL!'
"""

def disemvowel(string_):
    res = ""
    for symb in string_:
        if symb not in "aeuioAEUIO":
            res += symb
    return res
    