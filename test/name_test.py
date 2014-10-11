#!/usr/bin/env python
"""Unit tests for the Name class"""

from unittest import TestCase
from mock import Mock
from puckman.name import Name

class TestName(TestCase):
    def setUp(self):
        self.first_name = "Geoff"
        self.last_name = "Courtnall"
        self.name = Name(self.first_name, self.last_name)

    def test_creation(self):
        self.assertEqual(self.name.forename, self.first_name)
        self.assertEqual(self.name.surname, self.last_name)

    def test_full_name(self):
        self.assertEqual(self.name.full_name(), "Geoff Courtnall")

    def test_lexical_name(self):
        self.assertEqual(self.name.lexical_name(), "Courtnall, Geoff")

    def test_first_name_accessor(self):
        self.assertEqual(self.name.first_name(), self.first_name)

    def test_last_name_accessor(self):
        self.assertEqual(self.name.last_name(), self.last_name)

