#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.

It validates the matrix and divisor, ensuring correct types and dimensions,
and returns a new matrix with each element divided and rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The number to divide by.

    Returns:
        list of lists of float: A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(
           isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(
            isinstance(elem, (int, float))
            for row in matrix
            for elem in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if len({len(row) for row in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
