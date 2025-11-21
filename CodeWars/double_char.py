"""
Instructions:
Given a string, return a string in which each character (case-sensitive) is repeated once.

Examples:
"String"      -> "SSttrriinngg"
"Hello World" -> "HHeelllloo  WWoorrlldd"
"1234!_ "     -> "11223344!!__  "
"""

def double_char(s):
    l_s = (x*2 for x in s)
    fn = ''.join(l_s)
    return fn