#!/usr/bin/python3

"""Defining class square."""


class Square:
    """passing values to class objects."""

    def __init__(self, size=0, position=(0, 0)):
        """initilising object vsriables.

        Args:
            size (int): squire size sizes.
            position (tuple): squire co-ordinates.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def position(self):
        """Get position attribute."""
        return self.__positio

    @position.setter
    def position(self, position):
        self.__position = position

        if type(self.__position) is not tuple or len(self.__position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """calculate area."""
        return (self.__size * self.__size)

    def my_print(self):
        """print squire using '#' charactor."""
        if self.__size == 0:
            print("")
        elif self.__size > 0:
            for l in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print("")
