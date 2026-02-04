#!/usr/bin/python3
"""Module defining BaseGeometry and Rectangle classes."""


class BaseGeometry:
    """Base class for geometry objects with integer validation."""

    def area(self):
        """Raise an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): Name of the parameter for error messages.
            value (Any): Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
