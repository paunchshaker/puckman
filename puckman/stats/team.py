"""This module contains code describing a hockey team's season stats"""
from puckman.data_object import PMDataObject
from puckman.season import Season
from puckman.team import Team

from peewee import *

class TeamStats(PMDataObject):
    """Stats for a Team"""
    team = ForeignKeyField(Team, related_name='stats')
    season = ForeignKeyField(Season)

    wins = IntegerField(default=0)
    losses = IntegerField(default=0)
    ties = IntegerField(default=0)

    goals_for = IntegerField(default=0)
    goals_against = IntegerField(default=0)

    def add_win(self):
        """Add a win to the record."""
        self.wins += 1
        self.save()

    def add_loss(self):
        """Add a loss to the record."""
        self.losses += 1
        self.save()

    def add_tie(self):
        """Add a tie to the record."""
        self.ties += 1
        self.save()

    def add_goals_for(self, goals):
        self.goals_for += goals
        self.save()

    def add_goals_against(self, goals):
        self.goals_against += goals
        self.save()

