#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cp = my_list.copy()
    if idx < 0 or len(my_list_cp) <= idx:
        return my_list_cp
    my_list_cp[idx] = element
    return my_list_cp
