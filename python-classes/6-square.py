#!/usr/bin/python3
"""This module defines a Square class with size, position,
   area calculation, and printing functionality.
"""


class Square:
    """Represents a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): Position as (x, y). Defaults to (0, 0).

        Raises:
            TypeError: size must be int, position must be 2 positive ints tuple
            ValueError: size must be >= 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: Get or set the size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """tuple: Get or set the position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: Get or set the position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(x, int) for x in value)
            or not all(x >= 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """Print the square with '#' character, respecting the position."""
        if self.size == 0:
            print()
        else:
            for column in range(self.__position[1]):
                print()

            line = " " * self.__position[0] + "#" * self.__size
            for row in range(self.__size):
                print(line)
