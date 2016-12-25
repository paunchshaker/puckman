"""This module contains code describing a hockey player's season stats"""

from puckman.data_object import PMDataObject
from puckman.team import Team
from puckman.season import Season
from puckman.player import Player

from peewee import ForeignKeyField, IntegerField

class PlayerStats(PMDataObject):

    """Stats for a Player for a Season"""

    player = ForeignKeyField(Player, related_name='stats')
    season = ForeignKeyField(Season)
    team = ForeignKeyField(Team)

    goals = IntegerField(default=0)
    assists = IntegerField(default=0)

    # goalie stats
    wins = IntegerField(default=0)
    losses = IntegerField(default=0)
    ties = IntegerField(default=0)
    goals_allowed = IntegerField(default=0)
    shutouts = IntegerField(default=0)

    def add_goals(self, goals=1):
        """Add number of goals scored"""
        self.goals += goals
        self.save()

    def add_assists(self, assists=1):
        """Add number of assists scored"""
        self.assists += assists
        self.save()

    def add_wins(self, wins=1):
        """Add a goalie win"""
        self.wins += wins
        self.save()

    def add_losses(self, losses=1):
        """Add a goalie loss"""
        self.losses += losses
        self.save()

    def add_ties(self, ties=1):
        """Add a goalie tie"""
        self.ties += ties
        self.save()

    def add_goals_allowed(self, goals_allowed):
        """Add goalie allowed goals"""
        self.goals_allowed += goals_allowed
        self.save()

    def add_shutouts(self, shutouts=1):
        """Add goalie shutouts"""
        self.shutouts = shutouts
        self.save()



