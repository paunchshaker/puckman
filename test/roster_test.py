#!/usr/bin/env python
"""Unit tests for the Roster class"""

from unittest import TestCase
from puckman.roster import Roster
from puckman.player import Player
from puckman.name import Name

class TestRoster(TestCase):
    def setUp(self):
        self.roster = Roster()
        self.player1 = Player(Name(forename = "Trevor", surname = "Linden"), team = None, position = None)
        self.player2 = Player(Name(forename = "Scott", surname = "Pilgrim"), team = None, position = None)

    def test_creation(self):
        self.assertEqual(list(), self.roster.players())

    def test_add_player(self):
        self.roster.add_player(self.player1)
        self.assertEqual([self.player1], self.roster.players())

    def test_remove_player(self):
        self.roster.add_player(self.player1)
        self.roster.add_player(self.player2)
        self.roster.remove_player(self.player1)
        self.assertEqual([self.player2],self.roster.players())
