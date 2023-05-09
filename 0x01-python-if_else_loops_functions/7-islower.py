#!/usr/bin/python3
def islower(c):
    """Check if a character c is lowercase."""
    # Get the ASCII code for the character
    ascii_code = ord(c)
    
    # Check if the ASCII code is in the range of lowercase letters
    if ascii_code >= 97 and ascii_code <= 122:
        return True
    else:
        return False
