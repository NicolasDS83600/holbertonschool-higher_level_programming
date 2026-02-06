#!/usr/bin/python3
"""Module defining a Rectangle class by inheriting BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry with width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with validated width and height.

        Args:
            width (int): The width of the rectangle; must be > 0.
            height (int): The height of the rectangle; must be > 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
