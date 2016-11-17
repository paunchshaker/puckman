"""This module contains code describing a person in the most basic sense"""
from peewee import *
from puckman.data_object import PMDataObject

class Person(PMDataObject):

    """The Person class defines general info about all people."""
    forename = TextField()
    surname = TextField()

    def __init__(self, name):
        """Initialize a new Person"""
        super().__init__(forename=name.forename, 
                surname=name.surname)
        # NOTE Storing name here for historical reasons
        # May want to put in accessors to manage database updates through name
        # or make it read only, but for now leaving alone
        self.name = name

    def full_name(self):
        """Return a person full name e.g. Trevor Linden"""
        return self.name.full_name()
