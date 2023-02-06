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

    def __str__(self):
        """The informal representation of the rectangle"""
        return f'[Rectangle] {self.__width}/{self.__height}'

    def area(self):
        """Returns the area of a rectangle"""
        return self.__height * self.__width
