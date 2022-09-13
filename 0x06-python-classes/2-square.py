#!/usr/bin/python3

"""Defining new class Squire."""


class Square:
    """intilizing class attributes."""

    def __init__(self, size=0):
        """initilizing object variables.

        Args:
            size (int): squire sides size.
        """
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
