#!/usr/bin/python3
"""Define...."""


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file,
    after each line containing a specific string."""
    with open(filename, 'r+') as fd:
        contents = fd.readlines()
        if search_string in contents[-1]:
            contents.append(new_string)
        else:
            for index, line in enumerate(contents):
                if search_string in line:
                    contents.insert(index + 1, new_string)
        fd.seek(0)
        fd.writelines(contents)
