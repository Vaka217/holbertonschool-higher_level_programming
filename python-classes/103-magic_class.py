#!/usr/bin/python3

import math


class MagicClass:
    """ Class with methods to calculate area and circumference of a circle"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """ Circle area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Circle circumference"""
        return 2 * math.pi * self.__radius
