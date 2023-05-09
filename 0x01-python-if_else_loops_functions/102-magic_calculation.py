#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    return (c if a > b else a + b if c <= b else a * b - c)
