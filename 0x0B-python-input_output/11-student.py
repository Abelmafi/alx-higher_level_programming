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
            return self.__dict__
        for at in attrs:
            if not isinstance(at, str):
                return self.__dict__
        else:
            for attr in attrs:
                if attr in self.__dict__:
                    a[attr] = self.__dict__[attr]
            return a

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
        
