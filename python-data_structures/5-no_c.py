#!/usr/bin/env python3
def no_c(my_string):
    cp_str = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            cp_str += my_string[i]
    return cp_str
