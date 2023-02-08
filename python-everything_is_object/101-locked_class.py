#!/usr/bin/python3
""" locked class module"""


class LockedClass:
    """ Class with no attributes that prevents from creating new ones except
    for first_name"""
    __slots__ = ["first_name"]
