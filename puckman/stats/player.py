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

    def add_goals(self, goals=1):
        """Add number of goals scored"""
        self.goals += goals
        self.save()

    def add_assists(self, assists=1):
        """Add number of assists scored"""
        self.assists += assists
        self.save()

