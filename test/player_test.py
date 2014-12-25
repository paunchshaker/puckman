#!/usr/bin/env python
"""Unit tests for the Player class"""

from unittest import TestCase
from mock import Mock
from puckman.team import Team
from puckman.player import Player
from puckman.name import Name

class TestPlayer(TestCase):
    def setUp(self):
        self.team = Team(name = "Canucks", city = "Vancouver", skill = 100, record = None, abbreviation = "VAN")
        self.player = Player(Name(forename = "Cliff", surname = "Ronning"), team = self.team, position = "C")

    def test_creation(self):
        self.assertEqual(self.player.name, Name(forename = "Cliff", surname = "Ronning"))
        self.assertEqual(self.player.team, self.team)
        self.assertEqual(self.player.position, "C")
        self.assertIsNotNone(self.player.id)
