"""This module contains code describing a league"""

from puckman.data_object import PMDataObject
from peewee import TextField, DoesNotExist

class League(PMDataObject):

    """The League class defined information about a group of teams"""

    name = TextField()

    @property
    def current_season(self):
        """Return Season object representing current season for the league"""
        try:
            season = PMDataObject.deferred_relations['Season']
            return season.select().where(season.is_current == True,
                    season.league == self).get()
        except DoesNotExist:
            return None
