#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {x: 2 * a_dictionary[x] for x in a_dictionary.keys()}
    return new_dictionary
