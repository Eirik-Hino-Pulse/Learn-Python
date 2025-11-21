"""
Instructions:
Write a function feast that takes the animal's name (beast) and the dish as arguments and returns True or False to indicate whether the beast is allowed to bring the dish to the feast.

The dish must start and end with the same letters as the animal's name.
Assume that beast and dish are always lowercase strings, and each has at least two letters. 
Hyphens and spaces may occur, but will not appear at the beginning or end, and there will be no numerals.
"""

def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]: 
        return True 
    else: 
        return False
