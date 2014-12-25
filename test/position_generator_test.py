#!/usr/bin/env python
"""Unit tests for the PositionGenerator class"""

from unittest import TestCase
from mock import Mock
from puckman.position_generator import PositionGenerator

class TestPositionGenerator(TestCase):
    def test_creation(self):
        generator = PositionGenerator()
        self.assertIsNotNone(generator)
        self.assertIsNotNone(generator.generate())
