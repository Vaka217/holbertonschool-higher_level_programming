#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x + 1):
        try:
            print(my_list[i], end="")
        except IndexError:
            break
    print("")
    return i
