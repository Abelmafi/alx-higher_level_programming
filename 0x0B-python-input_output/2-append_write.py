#!/usr/bin/python3
"""defining....."""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file (UTF8)
    and returns the number of characters added."""

    with open(filename, 'a', encoding='utf-8') as f:
        num_char = f.write(text)

    return num_char
