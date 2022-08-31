#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = dict(a_dictionary)
    for i in new_dictionary.keys():
        new_dictionary[i] *= 2
    return (dict(new_dictionary))
