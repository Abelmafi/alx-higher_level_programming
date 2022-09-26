#!/usr/bin/python3
"""DEefine class named list."""


class MyList(list):
    """inherits from list."""

    def print_sorted(self):
        print(sorted(self))
