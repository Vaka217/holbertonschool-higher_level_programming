#!/usr/bin/python3
""" Module to object"""


import json


def to_json_string(my_obj):
    """ Returns an object (Python data structure)
    represented by a JSON string"""
    return json.dumps(my_obj)
