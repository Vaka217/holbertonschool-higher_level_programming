#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square by size and validates size
    Attributes:
        __size (int): Size of the square
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates area of a square
        """
        return self.__size ** 2
