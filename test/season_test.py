#!/usr/bin/env python
"""Unit tests for the Season class"""

from unittest import TestCase
from mock import Mock
from puckman.data_object import db
from puckman.league import League
from puckman.season import Season

class TestSeason(TestCase):
    def setUp(self):
        db.init(':memory:')
        db.create_tables([League, Season])

        self.league = League.create(name="Band Battle")
        self.season = Season.create(league=self.league, start_year=2016, end_year=2017)
    
    def test_creation(self):
        self.assertEqual(self.season.league, self.league)
        self.assertIsNotNone(self.season.id)
        self.assertEqual(self.season.start_year, 2016)
        self.assertEqual(self.season.end_year, 2017)

