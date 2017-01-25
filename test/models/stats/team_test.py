#!/usr/bin/env python
"""Unit tests for the TeamStats class"""

from unittest import TestCase
from puckman.database import Database
from sqlalchemy.orm import sessionmaker
from puckman.models.team import Team
from puckman.models.league import League
from puckman.models.season import Season
from puckman.models.stats.team import TeamStats


class TestTeamStats(TestCase):
    def setUp(self):
        self.db = Database.new_db()
        Session = sessionmaker(bind=self.db.engine)
        self.session = Session()

        self.league = League(name="Band Battle")
        self.season = Season(league=self.league,
                start_year=2016,
                end_year=2017,
                is_current=True)

        self.team = Team(name="Sex Bob-omb", 
                city="Toronto", 
                abbreviation="TOR", 
                league=self.league)

        self.team_stats = TeamStats(team=self.team,
                season=self.season)

        self.session.add_all([
            self.league,
            self.season,
            self.team,
            self.team_stats])
        self.session.commit()

    def test_add_win(self):
        self.team_stats.add_win()
        self.assertEqual(self.team_stats.wins, 1)

    def test_add_loss(self):
        self.team_stats.add_loss()
        self.assertEqual(self.team_stats.losses, 1)

    def test_add_tie(self):
        self.team_stats.add_tie()
        self.assertEqual(self.team_stats.ties, 1)

    def test_add_goals_for(self):
        self.team_stats.add_goals_for(2)
        self.assertEqual(self.team_stats.goals_for, 2)

    def test_add_goals_against(self):
        self.team_stats.add_goals_against(3)
        self.assertEqual(self.team_stats.goals_against, 3)
