#!/usr/bin/python3
"""Add command-line arguments to a JSON list stored in 'add_item.json'."""


import sys
from pathlib import Path

sys.path.append(".")

save_module = __import__("5-save_to_json_file")
save_to_json_file = save_module.save_to_json_file

load_module = __import__("6-load_from_json_file")
load_from_json_file = load_module.load_from_json_file

filename = "add_item.json"

if Path(filename).exists():
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
