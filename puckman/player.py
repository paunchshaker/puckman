"""This module contains code describing a player"""

from puckman.person import Person

class Player(Person):
    """The Player class defines general info about hockey players."""

    def __init__(self, first_name, last_name, position, team = None):
        """Initialize a new Player"""
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.position = position
