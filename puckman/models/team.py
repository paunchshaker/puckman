"""This module contains code describing a hockey team"""

from puckman.data_object import PMDataObject
from sqlalchemy import Column, Text, Integer, String, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship


class Team(PMDataObject):

    """The Team class defines information about a hockey team."""

    __tablename__ = 'teams'
    __table_args__ = (
        CheckConstraint('length(abbreviation) = 3'),
    )

    id = Column(Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship('League', back_populates='teams')

    name = Column(Text, nullable=False)
    city = Column(Text, nullable=False)
    abbreviation = Column(String(length=3), nullable=False)

    roster = relationship('Player', back_populates='team')
    stats = relationship('TeamStats', back_populates='team')

    # XXX Need to adapt the below to SQLAlchemy

#    def current_season_stats(self):
#        """Return the TeamStats object for the current season of this team"""
#        season_stats = PMDataObject.deferred_relations['TeamStats']
#        season = PMDataObject.deferred_relations['Season']
#        return season_stats.select().join(season).where(season.is_current == True, season_stats.team == self).get()
#
#    def won(self):
#        """Team has won a game"""
#        self.current_season_stats().add_win()
#
#    def lost(self):
#        """Team has lost a game"""
#        self.current_season_stats().add_loss()
#
#    def tied(self):
#        """Team tied a game"""
#        self.current_season_stats().add_tie()
#
#    def register_result(self, goals_for, goals_against):
#        """Register the result of a game"""
#        self.current_season_stats().add_goals_for(goals_for)
#        self.current_season_stats().add_goals_against(goals_against)

