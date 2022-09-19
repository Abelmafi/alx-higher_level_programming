#!/usr/bin/python3
"""Defines empty rectangle cass."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initilising object variables.

        Args:
            width (int): Rectangle width parameter.
            height (int): Rectangle height parameter.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width parameter."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get height parameter."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
