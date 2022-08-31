#!/usr/bin/python3
def roman_to_int(roman_string):
    base_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(roman_string)
    roman_number = 0
    i = 0
    if not roman_string:
        return (0)
    while i < len(roman_list):
        if roman_string[i] not in base_dict.keys():
            return (0)
        elif roman_list.count(roman_list[i]) > 3:
            return (0)
        elif i + 1 < len(roman_list):
            if base_dict[roman_list[i]] >= base_dict[roman_list[i + 1]]:
                roman_number += base_dict[roman_list[i]]
            else:
                roman_number += (base_dict[roman_list[i + 1]] - base_dict[roman_list[i]])
                i += 1
        else:
            roman_number += base_dict[roman_list[i]]
        i += 1
    return (roman_number)
