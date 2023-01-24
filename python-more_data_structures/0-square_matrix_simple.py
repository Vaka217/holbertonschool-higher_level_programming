#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for elements in matrix:
        square_matrix.append(list(map(lambda m: m ** 2, elements)))
    return square_matrix
