#!/usr/bin/python3
"""Module defining a Square class for learning OOP basics."""


class Square:
    """Represents a square with a size."""

    def __init__(self, size):
        """Initialize a Square with a given size.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
