#!/usr/bin/env python
"""Unit tests for the Person class"""

from unittest import TestCase
from puckman.database import Database
from sqlalchemy.orm import sessionmaker
from puckman.models.person import Person
from puckman.name import Name

class TestPerson(TestCase):
    def setUp(self):
        #self.db = Database.new_db()
        #Session = sessionmaker(bind=self.db.engine)
        #self.session = Session()

        self.name = Name(forename = "Trevor", surname = "Linden")
        self.person = Person(forename=self.name.forename, surname=self.name.surname)

    def test_creation(self):
        self.assertEqual(self.person.forename, self.name.forename)
        self.assertEqual(self.person.surname, self.name.surname)

    def test_creation_from_name(self):
        person2 = Person(name=self.name)
        self.assertEqual(person2.forename, self.name.forename)
        self.assertEqual(person2.surname, self.name.surname)

    def test_full_name(self):
        self.assertEqual(self.person.full_name(), "Trevor Linden")
