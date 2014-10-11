"""This module contains code describing a player"""

from puckman.person import Person

class Player(Person):
    """The Player class defines general info about hockey players."""

    def __init__(self, name,position, team=None):
        """Initialize a new Player"""
        super().__init__(name)
        self.team = team
        self.position = position
