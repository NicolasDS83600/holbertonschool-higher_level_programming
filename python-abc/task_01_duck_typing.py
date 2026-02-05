#!/usr/bin/python3
"""Defines abstract and concrete geometric shapes with area and perimeter."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape.

    Subclasses must implement methods to calculate area and perimeter.
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """Concrete implementation of a circle."""

    def __init__(self, radius):
        """Initialize a Circle with a given radius.

        Args:
            radius: Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete implementation of a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape.

    This function relies on duck typing. Any object passed in
    must implement area() and perimeter() methods.

    Args:
        shape: An object that provides area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
