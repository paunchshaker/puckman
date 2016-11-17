#!/usr/bin/env python
"""Unit tests for the Person class"""

from unittest import TestCase
from puckman.person import Person
from puckman.name import Name

class TestPerson(TestCase):
    def setUp(self):
        self.name = Name(forename = "Trevor", surname = "Linden")
        self.person = Person(self.name)

    def test_creation(self):
        self.assertEqual(self.person.name, self.name)
        self.assertEqual(self.person.forename, self.name.forename)
    def test_full_name(self):
        self.assertEqual(self.person.full_name(), "Trevor Linden")
