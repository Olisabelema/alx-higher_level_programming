#!/usr/bin/python3
def remove_char_at(s, n):
    # Create a new empty string to hold the result
    result = ""
    
    # Loop over the characters in the original string
    for i in range(len(s)):
        # Skip the character at index n
        if i == n:
            continue
        # Add all other characters to the result string
        result += s[i]
    
    # Return the result string
    return (result);
