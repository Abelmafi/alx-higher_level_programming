#!/usr/bin/python3
"""Defining..."""
from .base import Base


class Rectangle(Base):
    """Initilizing Rectangle class argumrnts."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width argument getter."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height argument getter."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x argument getter."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y argument getter."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        [print("") for l in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for k in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        """Tiht method assigns an argument to each args attribute."""
        ls = ["id", "width", "height", "x", "y"]
        if args:
            for index, arg in enumerate(args):
                setattr(self, ls[index], arg)
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangl."""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """return string representation of class attribute."""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                        self.id, self.__x, self.__y,
                                        self.__width, self.__height)
