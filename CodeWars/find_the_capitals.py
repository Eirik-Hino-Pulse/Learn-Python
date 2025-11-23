"""
Instructions
Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]
"""

def capitals(word):
    up_chraracher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ind_word = list(index1 for index1,symbol1 in enumerate(word) if symbol1 in up_chraracher)
    return ind_word