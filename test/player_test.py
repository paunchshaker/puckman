#!/usr/bin/env python
"""Unit tests for the Player class"""

from unittest import TestCase
from mock import Mock
from puckman.data_object import db, PMDataObject
from puckman.league import League
from puckman.team import Team
from puckman.person import Person
from puckman.player import Player
from puckman.name import Name

class TestPlayer(TestCase):
    def setUp(self):
        db.init(':memory:')
        db.create_tables(PMDataObject.__subclasses__())
        self.league = League.create(name="NHL")
        self.team = Team.create(name="Canucks",
                city="Vancouver",
                skill=100,
                abbreviation="VAN",
                league=self.league)
        self.person = Person.create_from_name(name=Name(forename = "Cliff",
            surname = "Ronning"))
        self.player = Player.create(person=self.person, team = self.team, position = "C")

    def test_creation(self):
        self.assertEqual(self.player.person.forename, "Cliff")
        self.assertEqual(self.player.person.surname, "Ronning")
        self.assertEqual(self.player.team, self.team)
        self.assertEqual(self.player.position, "C")
        self.assertIsNotNone(self.player.id)
