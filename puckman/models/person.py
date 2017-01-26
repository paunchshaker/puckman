"""This module contains code describing a person in the most basic sense"""
from puckman.data_object import PMDataObject
from puckman.name import Name
from sqlalchemy import Column, Text, Integer, String
from sqlalchemy.orm import composite

class Person(PMDataObject):

    """The Person class defines general info about all people."""
    
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    forename = Column(Text)
    surname = Column(Text)
    _type = Column(String(25))

    name = composite(Name, forename, surname)

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': '_type'
    }

    def full_name(self):
        return self.name.full_name()
