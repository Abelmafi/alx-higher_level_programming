#!/usr/bin/python3
def best_score(a_dictionary):
    max_num = 0
    num_key = ""
    if not a_dictionary:
        return (None)
    else:
        for i in a_dictionary:
            if a_dictionary[i] > max_num:
                max_num = a_dictionary[i]
                num_key = i
    return (num_key)
