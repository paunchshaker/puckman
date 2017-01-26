"""This module contains code describing a hockey team's season stats"""
from puckman.data_object import PMDataObject
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class TeamStats(PMDataObject):

    """Stats for a Team for a Season"""
    
    __tablename__ = 'teamstats'

    id = Column(Integer, primary_key=True)
    season_id = Column(Integer, ForeignKey('seasons.id'))
    season = relationship('Season')
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team', back_populates='stats')

    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    ties = Column(Integer, default=0)

    goals_for = Column(Integer, default=0)
    goals_against = Column(Integer, default=0)

    rank = Column(Integer, nullable=True)

    def add_win(self):
        """Add a win to the stats."""
        self.wins += 1

    def add_loss(self):
        """Add a loss to the stats."""
        self.losses += 1

    def add_tie(self):
        """Add a tie to the stats."""
        self.ties += 1

    def add_goals_for(self, goals):
        """Add goals scored to the stats."""
        self.goals_for += goals

    def add_goals_against(self, goals):
        """Add goals allowed to the stats."""
        self.goals_against += goals

