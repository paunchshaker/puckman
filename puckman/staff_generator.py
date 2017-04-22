"""This module generates staffers"""

from puckman.models.person import Person
from puckman.models.staff import Staff
from puckman.name_generator import NameGenerator
from numpy.random import normal

class StaffGenerator:

    """Generates Staff"""

    def __init__(self):
        """Initialize the generator"""
        self.name_generator = NameGenerator()

    def generate(self):
        name = self.name_generator.generate()
        return Staff(
                name=name,
                job="None"
                )
