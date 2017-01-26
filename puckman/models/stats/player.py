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

    def __init__(self, player, season, team):
        self.player = player
        self.season = season
        self.team = team

        self.goals = 0
        self.assists = 0
        self.shots = 0

        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.goals_allowed = 0
        self.shutouts = 0
        self.saves = 0

    def add_goals(self, goals=1):
        """Add number of goals scored"""
        self.goals += goals

    def add_assists(self, assists=1):
        """Add number of assists scored"""
        self.assists += assists

    def add_shots(self, shots=1):
        """Add shots taken"""
        self.shots += shots

    def add_wins(self, wins=1):
        """Add a goalie win"""
        self.wins += wins

    def add_losses(self, losses=1):
        """Add a goalie loss"""
        self.losses += losses

    def add_ties(self, ties=1):
        """Add a goalie tie"""
        self.ties += ties

    def add_goals_allowed(self, goals_allowed):
        """Add goalie allowed goals"""
        self.goals_allowed += goals_allowed

    def add_shutouts(self, shutouts=1):
        """Add goalie shutouts"""
        self.shutouts += shutouts

    def add_saves(self, saves=1):
        """Add goalie saves"""
        self.saves += saves

