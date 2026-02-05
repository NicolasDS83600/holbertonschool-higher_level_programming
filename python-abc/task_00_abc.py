#!/usr/bin/python3
"""Define an abstract Animal with concrete Dog and Cat implementations."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Concrete implementation of a dog."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Concrete implementation of a cat."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
