#!/usr/bin/python3
"""Module defining a Square class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle
    
class Square(Rectangle):
    """Square class inheriting from Rectangle with equal width and height."""

    def __init__(self, size):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square.

        Returns:
            str: Formatted as [Square] size/size.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
