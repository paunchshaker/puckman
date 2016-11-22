"""This module contains code describing a hockey team's season stats"""
from puckman.data_object import PMDataObject
from puckman.season import Season
from puckman.team import Team

from peewee import ForeignKeyField, IntegerField

class TeamStats(PMDataObject):

    """Stats for a Team for a Season"""
    
    team = ForeignKeyField(Team, related_name='stats')
    season = ForeignKeyField(Season)

    wins = IntegerField(default=0)
    losses = IntegerField(default=0)
    ties = IntegerField(default=0)

    goals_for = IntegerField(default=0)
    goals_against = IntegerField(default=0)

    def add_win(self):
        """Add a win to the stats."""
        self.wins += 1
        self.save()

    def add_loss(self):
        """Add a loss to the stats."""
        self.losses += 1
        self.save()

    def add_tie(self):
        """Add a tie to the stats."""
        self.ties += 1
        self.save()

    def add_goals_for(self, goals):
        """Add goals scored to the stats."""
        self.goals_for += goals
        self.save()

    def add_goals_against(self, goals):
        """Add goals allowed to the stats."""
        self.goals_against += goals
        self.save()

