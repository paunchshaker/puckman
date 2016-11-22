"""This module contains code handling a match between two teams"""
import numpy as np
import random

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
        self.assign_goals(self.home, home_goals)
        visitor_goals = np.random.poisson(self.visitor.skill)
        self.assign_goals(self.visitor, visitor_goals)

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

    def assign_goals(self, team, goals):
        if goals:
            skaters = [ x for x in team.roster if x.position != 'G' ]
            for g in range(goals):
                goal_scorer, first_assist, second_assist = random.sample(skaters, 3)
                goal_scorer.scored()
                first_assist.assisted()
                second_assist.assisted()
