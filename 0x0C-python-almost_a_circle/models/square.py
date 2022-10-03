#!/usr/bin/python3
"""Defining..."""
from .rectangle import Rectangle


class Square(Rectangle):
    """Initilizing Square parameters."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)
        #super().update(*args=(*args), **kwargs=(**kwargs))
        self.size = size

    @property
    def size(self):
        """Size attribute getter."""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Tiht method assigns an argument to each args attribute."""
        ls = ["id", "size", "x", "y"]
        for index, arg in enumerate(args):
            setattr(self, ls[index],arg)

        for key, values in kwargs.items():
            setattr(self, key, values)

    def to_dictionary(self):
        """Returns the dictionary representation of a Squire."""
        #return self.__dict__
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                self.id, self.x, self.y, self.width)
