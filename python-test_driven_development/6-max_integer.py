#!/usr/bin/python3
"""
This module provides a function to find the maximum integer in a list.
"""


def max_integer(list=[]):
    """
    Returns the maximum integer in a list.

    Args:
        list (list): List of integers or floats.

    Returns:
        int: The maximum value in the list.
        None if the list is empty.
    """
    if list is None:
        raise TypeError("list must be a list")
    if not list:
        return None
    max_val = list[0]
    for num in list:
        if num > max_val:
            max_val = num
    return max_val
