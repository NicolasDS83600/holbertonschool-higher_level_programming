#!/usr/bin/python3
"""Module that provides a function to list an object's attributes and methods."""


def lookup(obj):
    """Return a list of an object's attributes and methods.

    Args:
        obj: The object to inspect.

    Returns:
        list: Names of the object's attributes and methods.
    """
    return dir(obj)
