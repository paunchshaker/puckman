"""This module contains code handling a match between two teams"""
import random

class Game:

    """The Game class encapsulate the game simulation engine"""

    def __init__(self, home, visitor):
        self.home = home
        self.visitor = visitor

    def play(self):
        """Simulate a game"""
        cutoff = (self.home.skill - self.visitor.skill)/100 + 0.5
        if random.uniform(0, 1) < cutoff:
            self.home.won()
            self.visitor.lost()
        else:
            self.home.lost()
            self.visitor.won()
