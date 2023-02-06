#!/usr/bin/python3
"""Defines a class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Defines a class Rectangle"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
