#!/usr/bin/python3
"""Define BaseGeometry function."""


class BaseGeometry():
    """class with empty area methon."""

    def area(self):
        """raises an Exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """initilixing argument vriables."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__w = width
        self.__h = height

    def area(self):
        """returns area of rectangle."""
        return (self.__h * self.__w)

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__, self.__w, self.__h)
