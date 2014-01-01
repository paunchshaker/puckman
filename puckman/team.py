"""This module contains code describing a hockey team"""

class Team:
    """The Team class defines information about a hockey team."""

    def __init__(self, name, city, skill, record):
        """Initialize a new Team"""
        self.name = name
        self.city = city
        self.skill = skill
        self.record = record

    def won(self):
        """Team has won a game"""
        self.record.add_win()

    def lost(self):
        """Team has lost a game"""
        self.record.add_loss()
