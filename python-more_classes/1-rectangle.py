#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Defines a rectangle by width and height
    """
    def __init__(self, width=0, height=0):
        """
        init method
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = heigh