#!/usr/bin/env python
"""Unit tests for the Team class"""

from peewee import *
from unittest import TestCase
from mock import Mock
from puckman.data_object import db
from puckman.team import Team
from puckman.record import Record

class TestTeam(TestCase):
    def setUp(self):
        db.init(':memory:')
        db.create_tables([Team])
        self.team = Team.create(name = "Sex Bob-omb", city = "Toronto", skill = 90, record = Record(), abbreviation = "TOR")
        self.team.record
        #self.team.save()
    
    def test_creation(self):
        self.assertEqual(self.team.name, "Sex Bob-omb")
        self.assertEqual(self.team.city, "Toronto")
        self.assertEqual(self.team.skill, 90)
        self.assertEqual(self.team.record, Record())
        self.assertEqual(self.team.abbreviation, "TOR")
        self.assertEqual(self.team.goals_for, 0)
        self.assertEqual(self.team.goals_against, 0)
        self.assertIsNotNone(self.team.id)

    def test_bad_abbreviation(self):
        with self.assertRaises(IntegrityError):
            Team.create(name = "The Clash at Demonhead", city = "New York", skill = 50, record = Record(), abbreviation = "T")

    
    def test_win(self):
        self.team.won()
        self.assertEqual(self.team.record, Record(1,0))

    def test_loss(self):
        self.team.lost()
        self.assertEqual(self.team.record, Record(0,1))

    def test_tied(self):
        self.team.tied()
        self.assertEqual(self.team.record, Record(0,0,1))

    def test_register_results(self):
        self.team.register_result(5, 2)
        self.assertEqual(self.team.goals_for, 5)
        self.assertEqual(self.team.goals_against, 2)
