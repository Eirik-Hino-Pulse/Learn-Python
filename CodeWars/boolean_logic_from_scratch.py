"""
Instructions
Task:
You need to implement two functions, xor and or, that replicate the behaviour of their respective operators:

xor = Takes 2 values and returns true if, and only if, one of them is truthy.
or = Takes 2 values and returns true if either one of them is truthy. Do NOT use the or operator ||.

Input:
- Not all input will be booleans - there will be truthy and falsey values [the latter including also empty strings and empty arrays]
- There will always be 2 values provided.
"""

def func_or(a, b):
    if bool(a):
        return True
    elif bool(b):
        return True
    else:
        return False

def func_xor(a, b):
    return bool(a) != bool(b)