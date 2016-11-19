"""This module contains code describing a league"""
from puckman.data_object import PMDataObject
from peewee import *

class League(PMDataObject):
    """The League class defined information about a group of teams"""
    name = TextField()
    # NOTE Using IntegerField to store the id of the current season
    current_season = IntegerField(null=True)
