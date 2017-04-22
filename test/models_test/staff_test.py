#!/usr/bin/env python
"""Unit tests for the Staff class"""

from unittest import TestCase
from puckman.database import Database
from sqlalchemy.orm import sessionmaker
from puckman.models.league import League
from puckman.models.team import Team
from puckman.models.person import Person
from puckman.models.staff import Staff
from puckman.name import Name

class TestStaff(TestCase):
    def setUp(self):
        self.db = Database.new_db()
        Session = sessionmaker(bind=self.db.engine)
        self.session = Session()
        self.league = League(name="NHL")
        self.team = Team(name="Blues",
                city="Saint Louis",
                abbreviation="STL",
                league=self.league)
        self.staff = Staff(
                name=Name(forename = "Mike", surname = "Keenan"),
                team = self.team,
                job = "Head Coach",
                is_human=True
                )

        self.session.add_all([
                self.league,
                self.team,
                self.staff,
                ])
        self.session.commit()


    def test_creation(self):
        self.assertEqual(self.staff.name.forename, "Mike")
        self.assertEqual(self.staff.name.surname, "Keenan")
        self.assertEqual(self.staff.team, self.team)
        self.assertEqual(self.staff.job, "Head Coach")
        self.assertEqual(self.staff.is_human, True)
        self.assertIsNotNone(self.staff.id)
