#!/usr/bin/python3
""" 12-pascal_triangle module"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []
    lista = [[1]]
    for i in range(0, n - 1):
        sub = [1]
        for j in range(1, i + 1):
            sub.append(lista[i][j] + lista[i][j - 1])
        sub.append(1)
        lista.append(sub)
    return lista
