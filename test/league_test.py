#!/usr/bin/env python
"""Unit tests for the League and Season class"""

from unittest import TestCase
from mock import Mock
from puckman.data_object import db, PMDataObject
from puckman.league import League
from puckman.season import Season
from puckman.team import Team

class TestLeague(TestCase):
    def setUp(self):
        db.init(':memory:')
        db.create_tables([Team, League, Season])
        PMDataObject.deferred_relations['Season'] = Season

        self.league = League.create(name="Band Battle")
        self.season = Season.create(league=self.league,
                start_year=2016,
                end_year=2017,
                is_current=True)
        self.team = Team.create(name="Sex Bob-omb",
                city="Toronto",
                skill=90,
                abbreviation="TOR",
                league=self.league)
    
    def test_creation(self):
        self.assertEqual(self.league.name, "Band Battle")
        self.assertIsNotNone(self.league.id)
        self.assertEqual(self.league.current_season, self.season)

    def test_teams(self):
        self.assertIsNotNone(self.league.teams)
        self.assertEqual(self.league.teams[0].name, "Sex Bob-omb")
