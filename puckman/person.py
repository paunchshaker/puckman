"""This module contains code describing a person in the most basic sense"""
from uuid import uuid4

class Person:
    """The Person class defines general info about all people."""

    def __init__(self, name):
        """Initialize a new Person"""
        self.name = name
        self.uuid = uuid4()

    def full_name(self):
        """Return a person full name e.g. Trevor Linden"""
        return self.name.full_name()
