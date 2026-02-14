#!/usr/bin/python3
"""Defines a serializable CustomObject using pickle."""

import pickle


class CustomObject:
    """Represents a simple object that can be serialized."""

    def __init__(self, name, age, is_student):
        """Initialize object with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Save the object to a file using pickle."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PicklingError):
            return None
        return None

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    @classmethod
    def deserialize(cls, filename):
        """Load and return an object from a pickle file."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
        except (FileNotFoundError, OSError, pickle.UnpicklingError, EOFError):
            return None
        if not isinstance(obj, cls):
            return None
        return obj
