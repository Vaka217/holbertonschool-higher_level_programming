#!/usr/bin/python3
""" my_list module"""


class MyList(list):
    """ class that inherits from list"""
    def print_sorted(self):
        """ prints the list sorted"""
        print(sorted(self))
