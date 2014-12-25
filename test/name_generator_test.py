#!/usr/bin/env python
"""Unit tests for the Player class"""

from unittest import TestCase
from mock import Mock
from puckman.name_generator import NameGenerator

class TestPlayer(TestCase):
    def test_creation(self):
        generator = NameGenerator()
        self.assertIsNotNone(generator)
        self.assertIsNotNone(generator.generate())
