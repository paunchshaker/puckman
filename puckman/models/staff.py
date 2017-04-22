"""This module contains code describing staff"""

from puckman.models.person import Person
from sqlalchemy import Column, Boolean, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship

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
