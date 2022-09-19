#!/usr/bin/python3
"""Defines empty rectangle cass."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initilising object variables.

        Args:
            width (int): Rectangle width parameter.
            height (int): Rectangle height parameter.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """Returns printable chars using given character char."""

        if self.__height == 0 or self.__width == 0:
            return ("")

        str_t = []
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                str_t.append(str(self.print_symbol))
            if i < self.__height - 1:
                str_t.append('\n')
        return ("".join(str_t))

    def __repr__(self):
        """Retutrns  string representation of the rectangle to be able
        to recreate a new instance by using eval()"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return rec

    def __del__(self):
        print("Bye rectangle...")
        if Rectangle.number_of_instances >= 1:
            Rectangle.number_of_instances -= 1
