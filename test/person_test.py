#!/usr/bin/env python
"""Unit tests for the Person class"""

from unittest import TestCase
from puckman.person import Person
from puckman.name import Name
from puckman.data_object import db

class TestPerson(TestCase):
    def setUp(self):
        db.init(':memory:')
        db.create_tables([Person])

        self.name = Name(forename = "Trevor", surname = "Linden")
        self.person = Person.create(forename=self.name.forename, surname=self.name.surname)

    def test_creation(self):
        self.assertEqual(self.person.forename, self.name.forename)
        self.assertEqual(self.person.surname, self.name.surname)

    def test_creation_from_name(self):
        person2 = Person.create_from_name(self.name)
        self.assertEqual(person2.forename, self.name.forename)
        self.assertEqual(person2.surname, self.name.surname)

    def test_full_name(self):
        self.assertEqual(self.person.full_name(), "Trevor Linden")
