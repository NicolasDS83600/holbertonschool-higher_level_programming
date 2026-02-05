#!/usr/bin/env python3
"""Module defining mixin-based composition for swimming and flying."""


class SwimMixin:
    """Mixin providing swimming behavior."""

    def swim(self):
        """Print swimming ability."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying behavior."""

    def fly(self):
        """Print flying ability."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class composed using swim and fly mixins."""

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")
