"""This module contains code describing a season within a league"""

from puckman.data_object import PMDataObject
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Season(PMDataObject):

    """
    The Season class defines information about a League's
    season. It bridges stats to a season in time.
    """

    __tablename__ = 'seasons'
    
    id = Column(Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey('leagues.id'))
    is_current = Column(Boolean, default=True)
    start_year = Column(Integer, nullable=False)
    end_year = Column(Integer, nullable=False)
    
    league = relationship('League', back_populates='seasons')


