#!/usr/bin/python3
"""Appends text to a file and returns the number of characters written."""


def append_write(filename="", text=""):
    """Append text to a file and return the character count."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
