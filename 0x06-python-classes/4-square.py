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
        """str: size getter"""
        return self.__size

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
