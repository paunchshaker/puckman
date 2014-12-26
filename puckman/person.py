"""This module contains code describing a person in the most basic sense"""
from puckman.data_object import PMDataObject

class Person(PMDataObject):
    """The Person class defines general info about all people."""

    def __init__(self, name):
        """Initialize a new Person"""
        super().__init__()
        self.name = name

    def full_name(self):
        """Return a person full name e.g. Trevor Linden"""
        return self.name.full_name()
