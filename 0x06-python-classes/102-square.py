#!/usr/bin/python3

"""Defining class square."""


class Square:
    """passing values to class objects."""

    def __init__(self, size=0):
        """initilising object vsriables.

        Args:
            size (int): squire size sizes.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set current size of squire sides."""
        return (self.__size)

    @size.setter
    def size(self, size):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """calculates area.

        Returns:
            area of squire.
        """
        return (self.__size * self.__size)

    def __le__(self, other):
        """less than or equal to."""
        return self.__size <= other.__size

    def __lt__(self, other):
        """less than"""
        return self.__size < other.__size

    def __ge__(self, other):
        """greater than or equal with to"""
        return self.__size >= other.__size

    def __gt__(self, other):
        """greater than"""
        return self.__size > other.__size

    def __ne__(self, other):
        """not equal to."""
        return self.__size != other.__size

    def __eq__(self, other):
        """equal to."""
        return self.__size == other.__size
