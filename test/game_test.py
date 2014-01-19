#!/usr/bin/env python
"""Unit tests for the Game class"""

from unittest import TestCase
from mock import Mock
from puckman.team import Team
from puckman.game import Game
from puckman.record import Record

class TestGame(TestCase):
    def setUp(self):
        self.team1 = Team(name = "Sex Bob-omb", city = "Toronto", skill = 90, record = Record(), abbreviation = "SBO")
        self.team2 = Team(name = "The Clash at Demonhead", city = "New York", skill = 90, record = Record(), abbreviation = "TCD")
    
    def test_creation(self):
        game = Game(home = self.team1, visitor = self.team2)

        self.assertEqual(game.home, self.team1)
        self.assertEqual(game.visitor, self.team2)
    
    def test_play(self):
        self.team1.skill = 100
        self.team2.skill = 0
        game = Game(home = self.team1, visitor = self.team2)
        game.play()

        self.assertEqual(self.team1.record, Record(1,0))
        self.assertEqual(self.team2.record, Record(0,1))
        
        game = Game(home = self.team2, visitor = self.team1)
        game.play()
        self.assertEqual(self.team1.record, Record(2,0))
        self.assertEqual(self.team2.record, Record(0,2))

