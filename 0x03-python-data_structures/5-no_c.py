#!/usr/bin/python3
def no_c(my_string):
    result_str = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            result_str += my_string[i]
    return (result_str)
