#!/usr/bin/python3

"""Defining class square."""


class Square:
    """passing inital values to class object."""

    def __init__(self, size=0):
        """initilising object vsriables.

        Args:
            size (int): squire size sizes.
        """
        self.__size = size

    @property
    def size(self):
        """Get object attributes."""
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """calculate area of squire."""
        return (self.__size * self.__size)

    def my_print(self):
        """print suire using '#' charactors."""
        if self.__size == 0:
            print("")
        elif self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print("")
