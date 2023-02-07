#!/usr/bin/python3
""" Module to append a string to a text file"""


def append_write(filename="", text=""):
    """ Append a string to a text file (UTF8) and returns the number of
    characters written"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
