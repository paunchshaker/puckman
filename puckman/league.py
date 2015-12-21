"""This module contains code describing a league"""
from tabulate import tabulate
from puckman.data_object import PMDataObject
from puckman.roster import Roster

class League(PMDataObject):

    """The League class defined information about a group of teams"""

    def __init__(self, name, teams):
        """Initialize a new League"""
        super().__init__()
        self.name = name
        self.teams = teams
        self.roster = Roster()

    def __str__(self):
        standings = [[
            "{0} {1}".format(x.city, x.name),
            x.record.wins,
            x.record.losses,
            x.record.wins * 2] for x in
            sorted(self.teams,
                key=lambda team: team.record.wins * 2,
                reverse=True)]
        return tabulate(standings, headers=["Team", "Wins", "Losses", "Points"])

