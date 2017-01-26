#!/usr/bin/env python
"""Unit tests for the Season class"""

from unittest import TestCase
from puckman.database import Database
from sqlalchemy.orm import sessionmaker
from puckman.models.league import League
from puckman.models.season import Season

class TestSeason(TestCase):
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
        self.session.commit()
    
    def test_creation(self):
        self.assertEqual(self.season.league, self.league)
        self.assertIsNotNone(self.season.id)
        self.assertEqual(self.season.start_year, 2016)
        self.assertEqual(self.season.end_year, 2017)

