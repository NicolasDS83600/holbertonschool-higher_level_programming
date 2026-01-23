#!/usr/bin/python3
"""
This module provides a function for adding two numbers with type validation.

It ensures that only integers or floats are accepted, casts floats to integers,
and returns the sum as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result as an integer.

    Both a and b must be integers or floats. If a float is provided, it
    is first casted to an integer. Raises TypeError if any argument
    is not an integer or float.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
