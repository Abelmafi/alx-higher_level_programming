#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = dict(a_dictionary)
    for i in new_dict.keys():
        if i == key:
            del new_dict[key]
            break
        else:
            continue
    return (dict(new_dict))
