#!/usr/bin/python3

"""
divides all elements of a matrix


"""


def matrix_divided(matrix=None, div=None):
    """
    divides all elements of a matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or not
            all(isinstance(x, (int, float))
                for x in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda m: list(map(lambda x: round(x / div, 2), m)),
                    matrix))
