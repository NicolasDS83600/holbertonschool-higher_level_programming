#!/usr/bin/python3
"""Module defining a Rectangle class with width, height,
   area and perimeter attributes.
"""


class Rectangle:
    """Represents a rectangle shape with width and height.

    Attributes:
        number_of_instances (int): The number of Rectangle instances created.
        print_symbol: Symbol used for string representation of the rectangle.
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
