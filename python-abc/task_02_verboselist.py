#!/usr/bin/python3
"""A list subclass that prints notifications on modification operations."""


class VerboseList(list):
    """List that prints notifications when modified."""

    def append(self, item):
        """Add item to the list and print a notification."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Add all items from iterable and print a notification."""
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """Remove first occurrence of item and print a notification."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index and print a notification."""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
