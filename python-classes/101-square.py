#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square by size and validates size
    Attributes:
        __size (int): Size of the square
        __position (int, int): Coordinates of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ position getter"""
        return (self.__position)

    @position.setter
    def position(self, position):
        """ position setter"""
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all((isinstance(n, int) and n >= 0) for n in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Calculates area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        for h in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for z in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        """__str__ method"""
        printing = []
        if self.__size == 0:
            return ""
        for h in range(self.position[1]):
            printing.append('\n')
        for i in range(self.__size):
            if i > 0:
                printing.append('\n')
            for h in range(self.__position[0]):
                printing.append(" ")    
            for z in range(self.__position[0]):
                printing.append("")
            for j in range(self.__size):
                printing.append("#")
        return str(''.join(printing))
