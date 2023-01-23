#!/usr/bin/python3
def element_at(my_list, idx):
    if len(my_list) < idx or idx < 0:
        return None
    return my_list[idx]
