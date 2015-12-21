"""This module contains code describing a hockey team"""

from puckman.data_object import PMDataObject
from puckman.roster import Roster

class Team(PMDataObject):

    """The Team class defines information about a hockey team."""

    def __init__(self, name, city, skill, record, abbreviation):
        """Initialize a new Team"""
        super().__init__()
        self.name = name
        self.city = city
        self.skill = skill
        self.record = record
        self.roster = Roster()
        if len(abbreviation) == 3:
            self.abbreviation = abbreviation
        else:
            raise ValueError

    def won(self):
        """Team has won a game"""
        self.record.add_win()

    def lost(self):
        """Team has lost a game"""
        self.record.add_loss()
