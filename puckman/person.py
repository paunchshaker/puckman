"""This module contains code describing a person in the most basic sense"""

class Person:
    """The Person class defines general information about a person in the game world."""

    def __init__(self, first_name, last_name):
        """Initialize a new Person"""
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """Return a person full name e.g. Trevor Linden"""
        return " ".join((self.first_name, self.last_name))
