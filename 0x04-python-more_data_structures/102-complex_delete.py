#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    i = 0
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return (dict(a_dictionary))
