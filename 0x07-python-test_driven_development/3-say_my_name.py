#!/usr/bin/python3
"""Define name print function."""


def say_my_name(first_name, last_name=""):
    """Prints full name of a person."""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('first_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
