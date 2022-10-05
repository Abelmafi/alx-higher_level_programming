#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 3)
    r1_dictionary = {'id': 1, 'width': 3, 'height': 2, 'x': 5, 'y': 10}
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r1_dictionary)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
