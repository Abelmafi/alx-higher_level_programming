#!/usr/bin/python3
"""Defining...."""
import json


class Base:
    """Initilizing class attributes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base instants initilization."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json representation"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of json string.

        Args:
            json_string(str): json representation of str.
        Returns:
            json representation.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create dictionary representation of list object."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                rec = cls(1, 2)
            else:
                rec = cls(1)
            rec.update(**dictionary)
            return rec

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes."""
        try:
            with open(str(cls.__name__) + ".json", "r+") as fd:
                ls = fd.read()
                ls = cls.from_json_string(ls)
                bm = [cls.create(**i) for i in ls]
                return bm
        except IOError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """write json serialization of list of object to file."""
        with open(cls.__name__ + ".json", 'w+') as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                fd.write(cls.to_json_string(list_dicts))
