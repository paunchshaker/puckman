"""This module contains code describing a hockey team"""

from puckman.data_object import PMDataObject
from puckman.league import League

from collections import deque
from peewee import *

class Team(PMDataObject):

    """The Team class defines information about a hockey team."""
    league = ForeignKeyField(League, related_name='teams')

    name = TextField(null=False)
    city = TextField(null=False)
    skill = FloatField(null=False)
    abbreviation = CharField(max_length=3)

    class Meta:
        constraints = [Check('length(abbreviation) = 3')]

    def current_season_stats(self):
        for stats in self.stats:
            if stats.season == self.league.current_season:
                return stats

    def won(self):
        """Team has won a game"""
        self.current_season_stats().add_win()

    def lost(self):
        """Team has lost a game"""
        self.current_season_stats().add_loss()

    def tied(self):
        """Team tied a game"""
        self.current_season_stats().add_tie()

    def register_result(self, goals_for, goals_against):
        """Register the result of a game"""
        self.current_season_stats().add_goals_for(goals_for)
        self.current_season_stats().add_goals_against(goals_against)

