#!/usr/bin/env python
"""Unit tests for the Team class"""

from unittest import TestCase
from mock import Mock
from puckman.team import Team
from puckman.record import Record

class TestTeam(TestCase):
    def setUp(self):
        self.team = Team(name = "Sex Bob-omb", city = "Toronto", skill = 90, record = Record())
    
    def test_creation(self):
        self.assertEqual(self.team.name, "Sex Bob-omb")
        self.assertEqual(self.team.city, "Toronto")
        self.assertEqual(self.team.skill, 90)
        self.assertEqual(self.team.record, Record())
    
    def test_win(self):
        self.team.won()
        self.assertEqual(self.team.record, Record(1,0))

    def test_loss(self):
        self.team.lost()
        self.assertEqual(self.team.record, Record(0,1))

