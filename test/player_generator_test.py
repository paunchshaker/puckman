#!/usr/bin/env python
"""Unit tests for the PlayerGenerator class"""

from unittest import TestCase
from mock import Mock
from puckman.data_object import db
from puckman.player import Player
from puckman.person import Person
from puckman.player_generator import PlayerGenerator

class TestPlayerGenerator(TestCase):
    def test_creation(self):
        db.init(':memory:')
        db.create_tables([Player, Person])
        generator = PlayerGenerator()
        self.assertIsNotNone(generator)
        random_player = generator.generate()
        self.assertIsNotNone(random_player)
        self.assertIsNotNone(random_player.person)
        self.assertIsNotNone(random_player.position)
