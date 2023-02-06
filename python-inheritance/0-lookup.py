#!/usr/bin/python3
""" lookup moduel"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object"""
    return list(dir(obj))
