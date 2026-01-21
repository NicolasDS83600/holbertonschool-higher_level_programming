#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_diff1 = set_1 - set_2
    only_diff2 = set_2 - set_1
    only_diff1.update(only_diff2)
    return only_diff1
