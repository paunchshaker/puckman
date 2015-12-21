"""This module generates players"""

from puckman.player import Player
from puckman.name_generator import NameGenerator
from puckman.position_generator import PositionGenerator

class PlayerGenerator:

    """Generates players"""

    def __init__(self):
        """Initialize the generator"""
        self.name_generator = NameGenerator()
        self.position_generator = PositionGenerator()

    def generate(self):
        name = self.name_generator.generate()
        position = self.position_generator.generate()
        return Player(name, position)
