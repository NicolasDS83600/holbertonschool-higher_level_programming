#!/usr/bin/python3
"""Module that checks if an object inherits from a given class."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a subclass of a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj inherits from a_class but is not exactly a_class,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
