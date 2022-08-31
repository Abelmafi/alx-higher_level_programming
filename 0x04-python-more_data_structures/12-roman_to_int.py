#!/usr/bin/python3
def roman_to_int(roman_string):
    base = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_l = list(roman_string)
    roman_l = list(map(lambda x: x.upper(), roman_l))
    roman_number = 0
    i = 0
    if is_roman_num(roman_l) is False:
        return (0)
    while i < len(roman_l):
        if roman_l[i] not in base.keys():
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


def is_roman_num(roman_l=[]):
    if not roman_l:
        return (False)
    j = 0
    imp = []
    while j < len(roman_l):
        if imp:
            if imp[-1] == roman_l[j]:
                imp.append(roman_l[j])
            else:
                imp.clear()
        if len(imp) > 4:
            return (False)
        else:
            imp.append(roman_l[j])
        j += 1
    return (True)
