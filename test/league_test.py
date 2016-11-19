#!/usr/bin/env python
"""Unit tests for the League and Season class"""

from unittest import TestCase
from mock import Mock
from puckman.data_object import db
from puckman.league import League
from puckman.season import Season

class TestLeague(TestCase):
    def setUp(self):
        db.init(':memory:')
        db.create_tables([League, Season])

        self.league = League.create(name="Band Battle")
        self.season = Season.create(league=self.league, start_year=2016, end_year=2017)
        self.league.current_season = self.season.id
        self.league.save()
    
    def test_creation(self):
        self.assertEqual(self.league.name, "Band Battle")
        self.assertIsNotNone(self.league.id)
        self.assertEqual(self.league.current_season, self.season.id)
