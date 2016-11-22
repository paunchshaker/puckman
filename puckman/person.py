"""This module contains code describing a person in the most basic sense"""
from peewee import TextField
from puckman.data_object import PMDataObject
from puckman.name import Name

class Person(PMDataObject):

    """The Person class defines general info about all people."""

    forename = TextField()
    surname = TextField()

    @classmethod
    def create_from_name(cls, name):
        """Convenience method to create a person from a Name object"""
        return cls.create(forename=name.forename, surname=name.surname)

    def full_name(self):
        """Return a person full name e.g. Trevor Linden"""
        return Name(self.forename, self.surname).full_name()
