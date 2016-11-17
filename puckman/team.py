"""This module contains code describing a hockey team"""

from puckman.data_object import PMDataObject
from puckman.roster import Roster

from collections import deque
from peewee import *

class Team(PMDataObject):

    """The Team class defines information about a hockey team."""
    name = TextField(null=False)
    city = TextField(null=False)
    skill = FloatField(null=False)
    abbreviation = CharField(max_length=3)

    # Stats
    goals_for = IntegerField(default=0)
    goals_against = IntegerField(default=0)
    # Note Roster will move to a foreign key constraint on Player
    #self.roster = Roster()
    # Note Record will move to a foreign key constraint on Player as well.

    class Meta:
        constraints = [Check('length(abbreviation) = 3')]

    def won(self):
        """Team has won a game"""
        self.record.add_win()

    def lost(self):
        """Team has lost a game"""
        self.record.add_loss()

    def tied(self):
        """Team tied a game"""
        self.record.add_tie()

    def register_result(self, goals_for, goals_against):
        """Register the result of a game"""
        self.goals_for += goals_for
        self.goals_against += goals_against
        self.save()

