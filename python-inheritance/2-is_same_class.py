#!/usr/bin/python3
""" Check if an object is of certain class"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance
    of the specified class"""
    return issubclass(a_class, type(obj))
