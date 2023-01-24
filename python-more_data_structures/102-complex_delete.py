#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            keys.append(key)
    for key in keys:
        a_dictionary.pop(key)
    return a_dictionary
