#!/usr/bin/python3
"""Defining..."""


class Student:
    """intilizing Student attributes."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student."""
        a = {}
        if not attrs:
            return dict(reversed(list(self.__dict__.items())))
        else:
            for attr in attrs:
                if attr in self.__dict__:
                    a[attr] = self.__dict__[attr]
            return dict(reversed(list(a.items())))
