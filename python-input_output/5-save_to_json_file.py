#!/usr/bin/python3
"""Provides a utility to save Python objects to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a file in JSON format."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
