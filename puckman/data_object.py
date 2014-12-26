"""This module contains functionality that all Puckman data objects should
have"""

from uuid import uuid4

class PMDataObject:
    """The PMDataObject provides basic information for all data objects"""

    def __init__(self):
        """Initialize a new DataObject"""
        self.uuid = uuid4()

    def id(self):
        return self.uuid.hex