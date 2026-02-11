#!/usr/bin/python3
"""Reads and prints the contents of a UTF-8 text file."""


def read_file(filename=""):
    """Print the contents of a text file."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(content)
