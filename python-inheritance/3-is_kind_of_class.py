#!/usr/bin/python3
"""Module that checks if an object is an instance of a class or a subclass."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or its subclasses.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass,
              False otherwise.
    """
    return isinstance(obj, a_class)
