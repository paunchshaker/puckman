"""This module contains code describing a hockey team"""

from puckman.data_object import PMDataObject
from puckman.league import League

from peewee import ForeignKeyField, TextField, FloatField, CharField, Check

class Team(PMDataObject):

    """The Team class defines information about a hockey team."""

    league = ForeignKeyField(League, related_name='teams')

    name = TextField(null=False)
    city = TextField(null=False)
    skill = FloatField(null=False)
    abbreviation = CharField(max_length=3)

    class Meta:

        """Meta define information for the peewee ORM"""

        constraints = [Check('length(abbreviation) = 3')]

    def current_season_stats(self):
        """Return the TeamStats object for the current season of this team"""
        season_stats = PMDataObject.deferred_relations['TeamStats']
        season = PMDataObject.deferred_relations['Season']
        return season_stats.select().join(season).where(season.is_current == True, season_stats.team == self).get()

    def won(self):
        """Team has won a game"""
        self.current_season_stats().add_win()

    def lost(self):
        """Team has lost a game"""
        self.current_season_stats().add_loss()

    def tied(self):
        """Team tied a game"""
        self.current_season_stats().add_tie()

    def register_result(self, goals_for, goals_against):
        """Register the result of a game"""
        self.current_season_stats().add_goals_for(goals_for)
        self.current_season_stats().add_goals_against(goals_against)

