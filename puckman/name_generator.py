"""This module generates names"""

import random
from puckman.name import Name

class NameGenerator:

    """Generates names"""

    def __init__(self):
        """Load possible names"""
        self.first_names = ("Bob", "Bill", "Vladimir", "Sven")
        self.last_names = ("Jones", "Williams", "Federov", "Naslund")

    def generate(self):
        """Generate a random name"""
        return Name(forename = random.choice(self.first_names),
                surname = random.choice(self.last_names))

