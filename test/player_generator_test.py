#!/usr/bin/env python
"""Unit tests for the PlayerGenerator class"""

from unittest import TestCase
from mock import Mock
from puckman.player_generator import PlayerGenerator

class TestPlayerGenerator(TestCase):
    def test_creation(self):
        generator = PlayerGenerator()
        self.assertIsNotNone(generator)
        random_player = generator.generate()
        self.assertIsNotNone(random_player)
        self.assertIsNotNone(random_player.name)
        self.assertIsNotNone(random_player.position)
