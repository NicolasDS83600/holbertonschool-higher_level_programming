#!/usr/bin/python3
"""Module defining BaseGeometry and Rectangle classes."""

class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an exception indicating area is not implemented.

        Raises:
            Exception: Always raised because area() is not implemented.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): Name of the variable.
            value (Any): Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle.

        Returns:
            str: Formatted as [Rectangle] width/height.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
