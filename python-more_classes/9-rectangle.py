#!/usr/bin/python3
"""Module defining a Rectangle class with width, height,
   area, perimeter, and utility methods.
"""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances (int): Count of Rectangle instances.
        print_symbol (any): Symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle or
                 0 if either width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle using '#'.

        Returns:
            str: Lines representing the rectangle, or an empty string if
            width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string to recreate the rectangle with eval().

        Returns:
            str: "Rectangle(width, height)".
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Handle deletion of a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the larger area.

        If both rectangles have the same area, rect_1 is returned.

        Args:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.

        Returns:
            Rectangle: Rectangle with the greater or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a square rectangle (width == height == size).

        Args:
            size (int, optional): Size of the square sides. Defaults to 0.

        Returns:
            Rectangle: New Rectangle with width and height equal to size.
        """
        return cls(size, size)
