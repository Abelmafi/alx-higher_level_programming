#!/usr/bin/python3
def roman_to_int(roman_string):
    base = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_l = list(roman_string)
    roman_number = 0
    i = 0
    if not roman_string:
        return (0)
    while i < len(roman_l):
        if roman_string[i] not in base.keys():
            return (0)
        elif roman_l.count(roman_l[i]) > 3:
            return (0)
        elif i + 1 < len(roman_l):
            if base[roman_l[i]] >= base[roman_l[i + 1]]:
                roman_number += base[roman_l[i]]
            else:
                roman_number += (base[roman_l[i + 1]] - base[roman_l[i]])
                i += 1
        else:
            roman_number += base[roman_l[i]]
        i += 1
    return (roman_number)
