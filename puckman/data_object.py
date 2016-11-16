"""This module contains functionality that all Puckman data objects should have"""

from peewee import *

# Declare our intention to manage the db at runtime
db = SqliteDatabase(None)

class PMDataObject(Model):

    """The PMDataObject provides basic information for all data objects"""
    class Meta:
        database = db
