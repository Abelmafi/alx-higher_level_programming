#!/usr/bin/python3
"""Define....."""


def write_file(filename="", text=""):
    """This function that writes a string to a text file (UTF8)
    and returns the number of characters written."""

    with open(filename, 'w', encoding='utf-8') as f:
        num_ch = f.write(text)

    return num_ch
