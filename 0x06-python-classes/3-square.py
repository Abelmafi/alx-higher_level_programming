#!/usr/bin/python3

"""Defining class Square."""


class Square:
    """passing values to objects."""

    def __init__(self, size=0):
        """initilising object vsriables.

        Args:
            size (int): squire size sizes.
        """
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """calculate area of aquare.

        Returns:
            area size.
        """
        return (self.__size * self.__size)
