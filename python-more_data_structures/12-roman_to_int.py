#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    subtractive = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    entero = 0
    prev = ""
    for numbers in roman_string:
        if prev + numbers in subtractive:
            entero -= roman_dictionary.get(prev) * 2
        entero += roman_dictionary.get(numbers)
        prev = numbers
    return entero
