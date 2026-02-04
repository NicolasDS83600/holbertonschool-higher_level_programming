#!/usr/bin/python3
"""Module that defines a base geometry class."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an exception indicating the area is not implemented.

        Raises:
            Exception: Always raised to indicate the method is not implemented.
        """
        raise Exception("area() is not implemented")
