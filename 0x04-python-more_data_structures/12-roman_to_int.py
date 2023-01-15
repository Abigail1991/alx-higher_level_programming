#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    a = 0

    if type(roman_string) is str and roman string:
        for c in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[c]] >= a:
                res += val[roman-string[c]]
            else:
                res -= val[roman_string[c]]
            a = val[roman_string[c]]
            return res
