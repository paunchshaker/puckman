"""This module contains code describing staff"""

from puckman.models.person import Person
from sqlalchemy import Column, Boolean, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
import random

class Staff(Person):

    """The Staff class defined general info about non-player staff"""

    __tablename__ = 'staffers'

    id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=True)
    team = relationship('Team', back_populates='staff')
    job = Column(Enum("GM", "Head Coach", "None"), nullable=False)
    is_human = Column(Boolean, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'staff',
    }

    @staticmethod
    def non_negative(number):
        if number < 0:
            return 0
        else:
            return number

    @staticmethod
    def overall_player_score(shot_rate, scoring_rate):
        """Essentially take the F-measure of the stats"""
        try:
            return 2 * (shot_rate * scoring_rate) / (shot_rate + scoring_rate)
        except ZeroDivisionError:
            return 0

    def rate_player(self, player):
        """Give player an overall rating with some fudge"""
        standard_dev_on_eval = random.triangular(0.5, 2)
        eval_shot_rate = self.non_negative(random.gauss(player.shot_rate, standard_dev_on_eval))
        eval_scoring_rate = self.non_negative(random.gauss(player.scoring_rate, standard_dev_on_eval))
        return self.overall_player_score(eval_shot_rate, eval_scoring_rate)

    def evaluate_players(self, players):
        """This method generates evaluations for a list of players"""

        # TODO This should probably populate a table at some point, but for now
        # we will store as a variable
        self.ratings = { player.id: self.rate_player(player) for player in players }

    def choose_player(self, players):
        self.evaluate_players(players)
        ranked_players = sorted(players, reverse=True, key=lambda player: self.ratings[player.id])
        return ranked_players[0]



