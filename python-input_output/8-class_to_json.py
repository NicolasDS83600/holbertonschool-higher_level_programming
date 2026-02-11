#!/usr/bin/python3
"""Provides a function to convert an object's attributes to a dictionary."""


def class_to_json(obj):
    """Return the dictionary representation of an object."""
    return obj.__dict__
