#!/usr/bin/python3
"""MyInt"""


class MyInt(int):
    """Define int subclass."""

    def __init__(self, num):
        """initilizing MyInt args."""
        self.num = num

    def __str__(self):
        return str(self.num)

    def __eq__(self, num):
        return False

    def __ne__(self, num):
        return True
