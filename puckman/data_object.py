"""This module contains functionality that all Puckman data objects should have"""

from peewee import *

# Declare our intention to manage the db at runtime
db = SqliteDatabase(None)

class PMDataObject(Model):

    """The PMDataObject provides basic information for all data objects"""

    # NOTE This dict is intended to store references to classes that can't be
    # imported. It will need to be initialized with class objects outside of
    # this module.
    deferred_relations = dict()

    class Meta:

        """This defines Meta-information for the peewee ORM"""

        database = db
