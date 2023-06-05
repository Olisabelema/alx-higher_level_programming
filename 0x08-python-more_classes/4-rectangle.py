#!/usr/bin/python3
"This module defines a Rectangle class"


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """initializes the class

        Args:
            width (int, optional): width. Defaults to 0.
            height (int, optional): height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter

        Returns:
            int: rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value (int): new width

        Raises:
                        TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
