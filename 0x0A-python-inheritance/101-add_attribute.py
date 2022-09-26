#!/usr/bin/python3
"""this function that adds a new attribute to an object if it’s possible."""


def add_attribute(my_obj, name, attr):
    """Add a new attribute to an object if possible.
    Args:
        my_obj (any): The object to add an attribute to.
        name (str): The name of the attribute.
        attr (any): The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(my_obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(my_obj, name, attr)
