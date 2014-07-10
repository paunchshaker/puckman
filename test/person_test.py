#!/usr/bin/env/ python
"""Unit tests for the Person class"""

from unittest import TestCase
from puckman.person import Person

class TestPerson(TestCase):
    def setUp(self):
        self.person = Person(first_name = "Trevor", last_name = "Linden")

    def test_creation(self):
        self.assertEqual(self.person.first_name, "Trevor")
        self.assertEqual(self.person.last_name, "Linden")
    def test_full_name(self):
        self.assertEqual(self.person.full_name(), "Trevor Linden")
