#!/usr/bin/python3
"""Module adds all arguments to a Python list, and then save to a file"""

import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
with open(filename, 'a+', encoding="utf-8") as f:
    my_list = (load_from_json_file(filename)).extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
