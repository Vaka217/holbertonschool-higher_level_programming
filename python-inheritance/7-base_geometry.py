#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Defines a class BaseGeometry"""

    def area(self):
        """Public instance method that raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value is integer and greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
