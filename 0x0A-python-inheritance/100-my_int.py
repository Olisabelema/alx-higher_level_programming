#!/usr/bin/python3
"""
This module contains the MyInt Function
"""


class MyInt(int):
    """A class that inherits from Int"""
    def __eq__(self, other):
        """Override the equality comparison (==) to be inverted"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override the equality comparison (==) to be inverted"""
        return not super().__ne__(other)
