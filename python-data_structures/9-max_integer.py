#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    max = my_list[0]
    for val in my_list:
        if val > max:
            max = val
    return max
