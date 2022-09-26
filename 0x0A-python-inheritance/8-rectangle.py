#!/usr/bin/python3
"""Define BaseGeometry function."""


class BaseGeometry(object):
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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
