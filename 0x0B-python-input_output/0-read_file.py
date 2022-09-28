#!/usr/bin/python3
"""Define read_file() function."""


def read_file(filename=""):
    """This function reads a text file (UTF8) and prints it to stdout:"""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
