#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    return sum([n[0] * n[1] for n in my_list]) / sum([n[1] for n in my_list])
