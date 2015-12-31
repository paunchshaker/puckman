#!/usr/bin/env python
"""Unit tests for the Team class"""

from unittest import TestCase
from mock import Mock
from puckman.record import Record
from puckman.team import Team
from puckman.league import League

class TestLeague(TestCase):
    def setUp(self):
        self.team1 = Team(name = "Sex Bob-omb", city = "Toronto", skill = 90, record = Record(1,0), abbreviation = "SBO")
        self.team2 = Team(name = "Crash and the Boys", city = "Toronto", skill = 80, record = Record(0,1), abbreviation = "CAB")
        self.league = League(name="Band Battle", teams=[self.team1, self.team2])
    
    def test_creation(self):
        self.assertEqual(self.league.name, "Band Battle")
        self.assertListEqual(self.league.teams, [self.team1, self.team2])
        self.assertIsNotNone(self.league.id())

    def test_str(self):
        self.assertEqual(str(self.league), 
        "Team                          Wins    Losses    Ties    Points\n--------------------------  ------  --------  ------  --------\nToronto Sex Bob-omb              1         0       0         2\nToronto Crash and the Boys       0         1       0         0")

