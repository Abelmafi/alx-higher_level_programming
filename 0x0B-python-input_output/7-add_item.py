#!/usr/bin/python3
"""Defining...."""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import sys


def is_file_empty(file_name):
    """ Check if file is empty by reading first character in it"""

    with open(file_name, 'r') as read_obj:
        one_char = read_obj.read(1)
        if not one_char:
           return True
    return False


if __name__=='__main__':

    py_list = []

    f = open('add_item.json', 'a')
    f.close()
    if not is_file_empty('add_item.json'):
        py_list.extend(load_from_json_file('add_item.json'))
    for i in range(1, len(sys.argv)):
        py_list.append(sys.argv[i])
    save_to_json_file(py_list, 'add_item.json')
