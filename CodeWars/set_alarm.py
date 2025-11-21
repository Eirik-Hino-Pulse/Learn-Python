"""
Instructions:
Write a function named set_alarm which receives two parameters: employed and vacation (both boolean).
The function should return True if employed and not on vacation, otherwise False.

Examples:
employed | vacation | return
-------- | -------- | ------
 True    |  True    | False
 True    |  False   | True
 False   |  True    | False
 False   |  False   | False
"""

def set_alarm(employed, vacation):
    if employed == True and vacation == True:
        return False
    elif employed == True and vacation == False:
        return True
    elif employed == False and vacation == True:
        return False
    elif employed == False and vacation == False:
        return False 