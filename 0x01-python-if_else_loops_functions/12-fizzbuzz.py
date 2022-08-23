#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        if i % 3 == 0:
            print("{}".format("Fizz"), end=" ")
        elif i % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(i), end=" ")
