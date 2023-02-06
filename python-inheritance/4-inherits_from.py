#!/usr/bin/python3
""" Check if an object is an instance of the specified class"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class"""
    return isinstance(obj, a_class) and not issubclass(a_class, type(obj))
