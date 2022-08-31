#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary.keys():
        if i == key:
            a_dictionary[i] = value
        else:
            continue
    else:
        a_dictionary[key] = value
    return dict(a_dictionary)
