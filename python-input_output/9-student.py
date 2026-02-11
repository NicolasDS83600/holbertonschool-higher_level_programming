#!/usr/bin/python3
"""Defines a Student class with JSON-serializable attributes."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the student."""
        return self.__dict__
