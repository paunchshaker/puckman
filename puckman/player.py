"""This module contains code describing a player"""

from puckman.data_object import PMDataObject
from puckman.person import Person
from puckman.season import Season
from puckman.team import Team

from peewee import FixedCharField, ForeignKeyField, FloatField

class Player(PMDataObject):

    """The Player class defines general info about hockey players."""

    position = FixedCharField(max_length=1, null=False)
    person = ForeignKeyField(Person, related_name='player_role', null=False)
    team = ForeignKeyField(Team, related_name='roster', null=True)

    # skater skill levels
    # rate of scoring per 60 minutes
    scoring_rate = FloatField(null=False)
    # shot rate per 60 minutes
    shot_rate = FloatField(null=False)
    # shot suppression rate in shots reduced per 60 minutes
    #shot_suppression = FloatField(null=False)

    # scoring suppression. Goalies only for now. May want to split into two
    # ratings, one for skaters and one for goalies
    #scoring_suppression = FloatField(null=False)

    def current_team_season_stats(self):
        """Return the PlayerStats object for the current season and team"""
        stats = PMDataObject.deferred_relations['PlayerStats']
        current_season = Season.select(Season.id).where(Season.is_current==True).get()
        instance, create = stats.get_or_create(team=self.team,
                season=current_season, player=self)
        return instance

    def scored(self, goals=1):
        """Player scored a goal"""
        self.current_team_season_stats().add_goals(goals)

    def assisted(self, assists=1):
        """Player assisted on a goal"""
        self.current_team_season_stats().add_assists(assists)

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

