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
        self.simulate_scoring(self.home, self.visitor)

    def simulate_scoring(self, home, visitor):
        """Determine overall result of the game"""
        home_skaters = [x for x in home.roster if x.position != 'G']
        home_shot_rates = [x.shot_rate for x in home_skaters]
        home_total_shot_prob = sum(home_shot_rates)
        home_shot_probs = [x/home_total_shot_prob for x in home_shot_rates]
        away_skaters = [x for x in visitor.roster if x.position != 'G']
        away_shot_rates = [x.shot_rate for x in away_skaters]
        away_total_shot_prob = sum(away_shot_rates)
        away_shot_probs =[x/away_total_shot_prob for x in away_shot_rates]
        home_goalie = self.starting_goalie(home)
        away_goalie = self.starting_goalie(visitor)
        home_goals = 0
        visitor_goals = 0
        for shot in range(30):
            # each team gets 30 shots
            home_goals += self.simulate_shot(home_skaters, home_shot_probs,
                    away_goalie)
            visitor_goals += self.simulate_shot(away_skaters, away_shot_probs,
                    home_goalie)

        self.home.register_result(home_goals, visitor_goals)
        self.visitor.register_result(visitor_goals, home_goals)

        if visitor_goals == 0:
            home_goalie.shutout()
        if home_goals == 0:
            away_goalie.shutout()

        if home_goals > visitor_goals:
            home.won()
            home_goalie.won()
            visitor.lost()
            away_goalie.lost()
        elif visitor_goals > home_goals:
            home.lost()
            home_goalie.lost()
            visitor.won()
            away_goalie.won()
        else:
            home.tied()
            home_goalie.tied()
            visitor.tied()
            away_goalie.tied()

        return home_goals, visitor_goals

    def simulate_shot(self, skaters, shot_probs, goalie):
        """Simulate a single shot"""
        goal_scorer, first_assist, second_assist = np.random.choice(skaters, 3,
                replace=False, p=shot_probs)
        goal_scorer.shot()
        if np.random.binomial(n=1, p=goal_scorer.scoring_rate):
            goal_scorer.scored()
            first_assist.assisted()
            second_assist.assisted()
            goalie.allowed_goals(1)
            return 1
        else:
            goalie.made_save()
            return 0

    def starting_goalie(self, team):
        """Randomly choose goalie"""
        goalies = [ x for x in team.roster if x.position == 'G' ]
        return random.choice(goalies)
