"""This module contains code describing a player"""

from puckman.person import Person
from puckman.team import Team

from peewee import *

class Player(Person):

    """The Player class defines general info about hockey players."""
    position = FixedCharField(max_length=1)
    team = ForeignKeyField(Team, related_name='roster')

    def __init__(self, name, position, team=None):
        """Initialize a new Player"""
        super().__init__(name)
        self.team = team
        self.position = position
