#!/usr/bin/python3
"""
prints a square made of #
"""


def print_square(size):
    """Prints in stdout the square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
