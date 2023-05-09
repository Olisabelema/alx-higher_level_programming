#!/usr/bin/python3
def pow(a, b):
    """Compute a to the power of b and return the result."""
    result = 1
    for i in range(b):
        result *= a
    return (result)
