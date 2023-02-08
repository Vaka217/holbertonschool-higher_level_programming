#!/usr/bin/python3
""" append after module"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line
    containing a specific string"""
    with open(filename, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = lines[i] + new_string
        f.seek(0)
        for line in lines:
            f.write(line)
