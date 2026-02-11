#!/usr/bin/python3
"""Read and return Python objects from a JSON file."""

import json


def load_from_json_file(filename):
    """Load and return data from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
