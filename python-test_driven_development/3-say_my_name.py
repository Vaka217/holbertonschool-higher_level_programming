#!/usr/bin/python3

"""
prints "My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    checks if both parameters are strings and then prints them with the above format
    """
    if not first_name or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
