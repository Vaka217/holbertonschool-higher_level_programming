#!/usr/bin/python3
""" my int module"""


class MyInt(int):
    """ class that inhertis from int, but == and != are inverted"""
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
