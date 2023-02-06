#!/usr/bin/python3
""" Method with the class Square"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f'[Rectangle] {self.__size}/{self.__size}'
