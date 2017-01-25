"""This module generates players"""

from puckman.models.person import Person
from puckman.models.player import Player
from puckman.name_generator import NameGenerator
from puckman.position_generator import PositionGenerator
from numpy.random import normal

class PlayerGenerator:

    """Generates players"""

    def __init__(self):
        """Initialize the generator"""
        self.name_generator = NameGenerator()
        self.position_generator = PositionGenerator()

    def generate(self):
        name = self.name_generator.generate()
        position = self.position_generator.generate()
        scoring_rate = normal(loc=0.085, scale=0.02)
        if scoring_rate < 0.0:
            scoring_rate = 0.0
        shot_rate = normal(loc=6.0, scale=2.5)
        if shot_rate < 0.0:
            shot_rate = 0.0
        return Player(name=name, position=position,
                scoring_rate=scoring_rate,
                shot_rate=shot_rate)
