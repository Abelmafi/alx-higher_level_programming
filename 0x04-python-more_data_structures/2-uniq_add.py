#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_t = set(my_list)
    size = 0
    for i in set_t:
        size += i
    return size

