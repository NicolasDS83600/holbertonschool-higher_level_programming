#!/usr/bin/python3
"""Module defining a Square class with size validation and area calculation."""


class Square:
    """Represents a square with a validated size."""

    def __init__(self, size=0):
        """Initialize a Square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
