#!/usr/bin/python3
"""Module that contains the class Base"""


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        ++Base.__nb_objects
        self.id = Base.__nb_objects

