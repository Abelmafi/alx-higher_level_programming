#!/usr/bin/python3

"""jdjfjf"""

import math

"""kkdkdk"""


class MagicClass:
    """kfkfk"""

    def __init__(self, _MagicClass__radius=0):
        if ((type(_MagicClass__radius) is not int) and
                (type(_MagicClass__radius) is not float)):
            raise TypeError('radius must be a number')
        self._MagicClass__radius = _MagicClass__radius

    def area(self):
        return (math.pi * self._MagicClass__radius ** 2)

    def circumference(self):
        return (2 * math.pi * self._MagicClass__radius)
