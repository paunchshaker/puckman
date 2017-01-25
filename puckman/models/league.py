"""This module contains code describing a league"""

from puckman.data_object import PMDataObject
from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

class League(PMDataObject):

    """The League class defined information about a group of teams"""
    
    __tablename__ = 'leagues'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    teams = relationship('Team', back_populates='league')
    seasons = relationship('Season', back_populates='league')

    @hybrid_property
    def current_season(self):
        """Return Season object representing current season for the league"""
        if self.seasons:
            return self.seasons[0]
        else:
            return None
