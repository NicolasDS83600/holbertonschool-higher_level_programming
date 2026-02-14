#!/usr/bin/python3
"""Functions to serialize data to JSON and read it back from a file."""

import json


def serialize_and_save_to_file(data, filename):
    """Save Python data as JSON to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load JSON data from a file and return as Python objects."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
