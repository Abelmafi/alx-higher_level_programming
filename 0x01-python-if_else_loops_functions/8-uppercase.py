#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >=97 and ord(i) <= 122:
                i = ord(i) - 32
                print(chr(i), end="")
        else:
            print(i, end="")
    print()

