#!/usr/bin/python3

"""Defining class square."""


class Square:
    """passing values to class objects."""

    def __init__(self, size=0, position=(0, 0)):
        """Initilising object variables.

        Args:
            size (int): squire size sizes.
            position (int, int): squire co-ordinates position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position attribute."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return calculated area."""
        return (self.__size * self.__size)

    def my_print(self):
        """print squire using '#' charactor."""
        if self.__size == 0:
            print("")
            return

        [print("") for l in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for k in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print("")
