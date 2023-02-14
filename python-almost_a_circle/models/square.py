#!/usr/bin/python3
""" module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class that defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization for square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ __str__ method"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}")

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """ size setter"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        if args and len(args) > 0:
            attr = ["id", "size", "x", "y"]
            i = 0
            for argv in args:
                setattr(self, attr[i], argv)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
