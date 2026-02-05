#!/usr/bin/env python3
"""Module defining multiple inheritance and method resolution order."""


class Fish:
    """Fish class with swimming behavior."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class with flying behavior."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class demonstrating multiple inheritance from Fish and Bird."""

    def fly(self):
        """Override fly behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat behavior."""
        print("The flying fish lives both in water and the sky!")
