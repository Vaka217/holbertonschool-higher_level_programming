#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square by size and validates size
    Attributes:
        __size (int): Size of the square
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Calculates area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """ size setter"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
