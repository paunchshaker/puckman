"""This module contains code describing a hockey player's season stats"""

from puckman.data_object import PMDataObject
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class PlayerStats(PMDataObject):

    """Stats for a Player for a Season"""

    __tablename__ = 'playerstats'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship('Player', back_populates='stats')
    season_id = Column(Integer, ForeignKey('seasons.id'))
    season = relationship('Season')
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team')

    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    shots = Column(Integer, default=0)

    # goalie stats
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    ties = Column(Integer, default=0)
    goals_allowed = Column(Integer, default=0)
    shutouts = Column(Integer, default=0)
    saves = Column(Integer, default=0)

    # XXX Switch to SQLAlchemy

    def add_goals(self, goals=1):
        """Add number of goals scored"""
        self.goals += goals
        self.save()

    def add_assists(self, assists=1):
        """Add number of assists scored"""
        self.assists += assists
        self.save()

    def add_shots(self, shots=1):
        """Add shots taken"""
        self.shots += shots
        self.save()

    def add_wins(self, wins=1):
        """Add a goalie win"""
        self.wins += wins
        self.save()

    def add_losses(self, losses=1):
        """Add a goalie loss"""
        self.losses += losses
        self.save()

    def add_ties(self, ties=1):
        """Add a goalie tie"""
        self.ties += ties
        self.save()

    def add_goals_allowed(self, goals_allowed):
        """Add goalie allowed goals"""
        self.goals_allowed += goals_allowed
        self.save()

    def add_shutouts(self, shutouts=1):
        """Add goalie shutouts"""
        self.shutouts += shutouts
        self.save()

    def add_saves(self, saves=1):
        """Add goalie saves"""
        self.saves += saves
        self.save()



