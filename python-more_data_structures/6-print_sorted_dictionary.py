#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for v in sorted(a_dictionary):
        print(v, a_dictionary[v], sep=": ")
