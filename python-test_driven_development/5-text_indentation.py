#!/usr/bin/python3
"""
This module provides a function for printing text with indentation after
specific punctuation characters.

It prints two new lines after each '.', '?', or ':'. Leading and trailing
spaces are removed from each line.
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each '.', '?', or ':'.

    Removes spaces at the beginning and end of each printed line.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    start = 0
    has_punct = False

    for i, char in enumerate(text):
        if char in punctuation:
            line = text[start:i+1].strip()
            print(line)
            print()
            has_punct = True
            start = i + 1
    if start < len(text):
        line = text[start:].strip()
        if line:
            if has_punct:
                print(line)
            else:
                print(line, end="")