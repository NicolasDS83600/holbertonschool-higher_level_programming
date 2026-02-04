#!/usr/bin/python3
"""Module that defines a Mylist class with a sorted print method."""


class MyList(list):
    """Custom list class which print its elements in sorted order."""

    def print_sorted(self):
        """Print the list elements in ascending order."""
        print(sorted(self))
