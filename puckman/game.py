"""This module contains code handling a match between two teams"""
import numpy as np

class Game:

    """The Game class encapsulate the game simulation engine"""

    def __init__(self, home, visitor):
        self.home = home
        self.visitor = visitor

    def play(self):
        """Simulate a game"""
        home_goals = np.random.poisson(self.home.skill)
        visitor_goals = np.random.poisson(self.visitor.skill)
        self.home.register_result(home_goals, visitor_goals)
        self.visitor.register_result(visitor_goals, home_goals)
        if home_goals >= visitor_goals:
            self.home.won()
            self.visitor.lost()
        else:
            self.home.lost()
            self.visitor.won()
