#!/usr/bin/python3
"""Provides a helper function to deserialize JSON strings."""

import json


def from_json_string(my_str):
    """Return a Python object from a JSON string."""
    return json.loads(my_str)
