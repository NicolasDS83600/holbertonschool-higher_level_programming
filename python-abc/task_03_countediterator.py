#!/usr/bin/env python3
"""Module defining a counted iterator that tracks items fetched."""


class CountedIterator:
    """Iterator class that counts items fetched."""

    def __init__(self, iterable):
        """Initialize with iterable and set counter to zero."""
        self._iterator = iter(iterable)
        self._count = 0

    def __next__(self):
        """Return next item and increment the counter."""
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        """Return number of items fetched so far."""
        return self._count
