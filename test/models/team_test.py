#!/usr/bin/env python
"""Unit tests for the Team class"""

from unittest import TestCase
from puckman.database import Database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from puckman.models.team import Team
from puckman.models.league import League
from puckman.models.season import Season
from puckman.models.stats.team import TeamStats

class TestTeam(TestCase):
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
    
    def test_creation(self):
        self.assertEqual(self.team.league, self.league)
        self.assertEqual(self.team.name, "Sex Bob-omb")
        self.assertEqual(self.team.city, "Toronto")
        self.assertEqual(self.team.abbreviation, "TOR")
        self.assertIsNotNone(self.team.id)

    def test_bad_abbreviation(self):
        with self.assertRaises(IntegrityError):
            team = Team(name = "The Clash at Demonhead", city = "New York", abbreviation = "T")
            self.session.add(team)
            self.session.commit()

    def test_current_season_stats(self):
        self.assertEqual(self.team.current_season_stats().id,
                self.team_stats.id)
    
    def test_win(self):
        self.team.won()
        self.assertEqual(self.team.current_season_stats().wins, 1)

    def test_loss(self):
        self.team.lost()
        self.assertEqual(self.team.current_season_stats().losses, 1)

    def test_tied(self):
        self.team.tied()
        self.assertEqual(self.team.current_season_stats().ties, 1)

    def test_register_results(self):
        self.team.register_result(5, 2)
        self.assertEqual(self.team.current_season_stats().goals_for, 5)
        self.assertEqual(self.team.current_season_stats().goals_against, 2)
