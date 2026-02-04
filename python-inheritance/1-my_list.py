#!/usr/bin/python3
"""Module that defines a Mylist class with a sorted print method."""


class Mylist(list):
    """Custom list class with a method to print its elements in sorted order."""

    def print_sorted(self):
        """Print the list elements in ascending order."""
        print(sorted(self))
