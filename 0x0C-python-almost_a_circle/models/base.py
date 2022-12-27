#!/usr/bin/python3
"""Defining...."""
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from <cls.__name__>.csv.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
