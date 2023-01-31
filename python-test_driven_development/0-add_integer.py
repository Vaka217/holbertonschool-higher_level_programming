#!/usr/bin/python3

""" adds two numbers and returns the result"""


def add_integer(a, b=98):
    """ checks if a and b are numbers and then return their integer sum"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
