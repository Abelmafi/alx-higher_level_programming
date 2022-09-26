#!/usr/bin/python3
"""Define BaseGeometry function."""
BaseGeometry = __import__('9-rectangle').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Return the area of square."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
