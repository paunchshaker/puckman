"""This module contains code describing a league"""
from puckman.data_object import PMDataObject
from peewee import *

class League(PMDataObject):
    """The League class defined information about a group of teams"""
    name = TextField()

    @property
    def current_season(self):
        for season in self.seasons:
            if season.is_current:
                return season
         
