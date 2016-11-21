"""This module contains code describing a player"""

from puckman.data_object import PMDataObject
from puckman.person import Person
from puckman.team import Team

from peewee import *

class Player(PMDataObject):

    """The Player class defines general info about hockey players."""
    position = FixedCharField(max_length=1, null=False)
    person = ForeignKeyField(Person, related_name='player_role', null=False)
    team = ForeignKeyField(Team, related_name='roster', null=True)
