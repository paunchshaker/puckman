"""This module contains code describing a season within a league"""
from puckman.data_object import PMDataObject
from puckman.league import League

from peewee import ForeignKeyField, BooleanField, IntegerField

class Season(PMDataObject):

    """
    The Season class defines information about a League's
    season. It bridges stats to a season in time.
    """
    
    league = ForeignKeyField(League, related_name='seasons', null=False)
    is_current = BooleanField(default=True)
    start_year = IntegerField(null=False)
    end_year = IntegerField(null=False)

