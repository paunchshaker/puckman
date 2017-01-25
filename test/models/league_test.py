#!/usr/bin/env python
"""Unit tests for the League and Season class"""

from unittest import TestCase
from mock import Mock
from puckman.database import Database
from sqlalchemy.orm import sessionmaker
from puckman.models.league import League
from puckman.models.season import Season
from puckman.models.team import Team

class TestLeague(TestCase):
    def setUp(self):
        self.db = Database.new_db()
        Session = sessionmaker(bind=self.db.engine)
        self.session = Session()
        self.league = League(name="Band Battle")
        self.session.add(self.league)
        self.season = Season(league=self.league,
                start_year=2016,
                end_year=2017,
                is_current=True)
        self.session.add(self.season)
        self.team = Team(name="Sex Bob-omb",
                city="Toronto",
                abbreviation="TOR",
                league=self.league)
        self.session.add(self.team)
        self.session.commit()
    
    def test_creation(self):
        self.assertEqual(self.league.name, "Band Battle")
        self.assertIsNotNone(self.league.id)
        self.assertEqual(self.league.current_season, self.season)

    def test_no_current_season(self):
        self.season.is_current = False
        self.session.commit()
        self.assertIsNone(self.league.current_season)

    def test_teams(self):
        self.assertIsNotNone(self.league.teams)
        self.assertEqual(self.league.teams[0].name, "Sex Bob-omb")
