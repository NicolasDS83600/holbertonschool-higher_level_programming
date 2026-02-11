#!/usr/bin/python3
"""Defines a Student class with JSON serialization support."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary of the student's attrs, optionally filtered."""
        if isinstance(attrs, list):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
                }
        else:
            return self.__dict__
