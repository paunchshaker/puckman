"""This module generates players"""

from puckman.person import Person
from puckman.player import Player
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
        person = Person.create_from_name(name)
        person.save()
        scoring_rate = normal(loc=0.08, scale=0.02) - 0.01
        if scoring_rate < 0.0:
            scoring_rate = 0.0
        shot_rate = normal(loc=6.0, scale=2.5)
        if shot_rate < 0.0:
            shot_rate = 0.0
        return Player.create(person=person, position=position,
                scoring_rate=scoring_rate,
                shot_rate=shot_rate)
