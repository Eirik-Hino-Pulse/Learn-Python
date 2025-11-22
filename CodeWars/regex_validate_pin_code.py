"""
Instructions:
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
"""

def validate_pin(pin):
    if len(pin) == 4 and pin.isdigit() or len(pin) == 6 and pin.isdigit():
        return True
    elif len(pin) != 4 and not pin.isdigit() or len(pin) != 6 and not pin.isdigit():
        return False
    else:
        return False