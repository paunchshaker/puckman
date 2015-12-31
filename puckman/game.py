"""This module contains code handling a match between two teams"""
import numpy as np

class Game:

    """The Game class encapsulate the game simulation engine"""

    def __init__(self, home, visitor):
        self.home = home
        self.visitor = visitor

    def play(self):
        """
        Simulate a game
        
        Currently uses a poisson distribution where \lambda is the number of
        goals per game. There is no concept of defense.

        See http://www.hockeyanalytics.com/Research_files/Poisson_Toolbox.pdf
        """
        home_goals = np.random.poisson(self.home.skill)
        visitor_goals = np.random.poisson(self.visitor.skill)
        self.home.register_result(home_goals, visitor_goals)
        self.visitor.register_result(visitor_goals, home_goals)
        if home_goals > visitor_goals:
            self.home.won()
            self.visitor.lost()
        elif visitor_goals > home_goals:
            self.home.lost()
            self.visitor.won()
        else:
            self.home.tied()
            self.visitor.tied()
