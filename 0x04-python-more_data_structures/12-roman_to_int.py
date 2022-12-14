#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return (0)
    base = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_l = list(roman_string)
    roman_l = list(map(lambda x: x.upper(), roman_l))
    roman_number = 0
    i = 0
    while i < len(roman_l):
        if i + 1 < len(roman_l):
            if base[roman_l[i]] >= base[roman_l[i + 1]]:
                roman_number += base[roman_l[i]]
            else:
                roman_number += base[roman_l[i + 1]] - base[roman_l[i]]
                i += 1
        else:
            roman_number += base[roman_l[i]]
        i += 1
    return (roman_number)
