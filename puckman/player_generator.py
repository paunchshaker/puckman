"""This module generates players"""

from puckman.person import Person
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
        person = Person.create_from_name(name)
        person.save()
        return Player.create(person=person, position=position)
