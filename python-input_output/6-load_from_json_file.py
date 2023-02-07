#!/usr/bin/python3
""" Module to create an Object"""


import json


def load_from_json_file(filename):
    """  Creates an Object from a JSON file"""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
