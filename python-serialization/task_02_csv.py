#!/usr/bin/python
"""Utility to convert a CSV file into a JSON file."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format."""
    try:
        with open(csv_filename, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False

    except Exception:
        return False
