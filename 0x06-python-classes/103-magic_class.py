#!/usr/bin/python3
import math

"""kkdkdk"""


class MagicClass:
    """kfkfk"""

    def __init__(self, _MagicClass__radius=0):
        self._MagicClass__radius = _MagicClass__radius

    def radius(self, radius):
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        return (math.pi * self._MagicClass__radius ** 2)

    def circumference(self):
        return (2 * math.pi * self._MagicClass__radius)

mc = MagicClass(10)
print("{:.2f}".format(mc.circumference()))
