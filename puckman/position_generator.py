"""This modeule generates player positions"""
import random

class PositionGenerator:
    """Generate positions"""

    def __init__(self):
        """Load up possible positions and their intended frequencies"""
        self.positions = ( "RD", "LD", "G", "C", "LW", "RW", "C" )

    def generate(self):
        return random.choice(self.positions)
