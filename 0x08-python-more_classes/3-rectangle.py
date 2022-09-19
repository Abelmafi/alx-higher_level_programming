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

    def area(self):
        """Returns area or rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter or rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns printable chars using # char."""

        if self.__height == 0 or self.__width == 0:
            return ("")
        str_t = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                str_t += '#'
            if i < self.__height - 1:
                str_t += '\n'
        return "{}".format(str_t)
