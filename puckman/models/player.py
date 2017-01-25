"""This module contains code describing a player"""

from puckman.models.person import Person
from puckman.models.season import Season
from puckman.models.stats.player import PlayerStats
from sqlalchemy import Column, Integer, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship

class Player(Person):

    """The Player class defines general info about hockey players."""

    __tablename__ = 'players'

    id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    position = Column(Enum("RD", "LD", "G", "C", "LW", "RW", "C"), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=True)
    team = relationship('Team', back_populates='roster')
    stats = relationship('PlayerStats', back_populates='player')

    # skater skill levels
    # rate of scoring per 60 minutes
    scoring_rate = Column(Float, nullable=False)
    # shot rate per 60 minutes
    shot_rate = Column(Float, nullable=False)
    # shot suppression rate in shots reduced per 60 minutes
    #shot_suppression = FloatField(null=False)

    # scoring suppression. Goalies only for now. May want to split into two
    # ratings, one for skaters and one for goalies
    #scoring_suppression = FloatField(null=False)

    __mapper_args__ = {
        'polymorphic_identity': 'player',
    }


    def current_team_season_stats(self):
        """Return the PlayerStats object for the current season and team"""
        for stats in self.stats:
            if stats.season.is_current and stats.team == self.team:
                return stats
        else:
            current_season = self.team.league.current_season
            return PlayerStats(team=self.team, season=current_season,
                    player=self)

    def scored(self, goals=1):
        """Player scored a goal"""
        self.current_team_season_stats().add_goals(goals)

    def assisted(self, assists=1):
        """Player assisted on a goal"""
        self.current_team_season_stats().add_assists(assists)

    def shot(self):
        """Player had a shot"""
        self.current_team_season_stats().add_shots()

    def won(self):
        """Player won a game"""
        self.current_team_season_stats().add_wins()
    
    def lost(self):
        """Player lost a game"""
        self.current_team_season_stats().add_losses()

    def tied(self):
        """Player tied a game"""
        self.current_team_season_stats().add_ties()

    def allowed_goals(self, goals_allowed):
        """Player allowed goals"""
        self.current_team_season_stats().add_goals_allowed(goals_allowed)

    def shutout(self):
        """Player had a shutout"""
        self.current_team_season_stats().add_shutouts()

    def made_save(self):
        """Player made a save"""
        self.current_team_season_stats().add_saves()

