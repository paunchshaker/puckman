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
from puckman.season import Season
from puckman.stats.player import PlayerStats

class TestPlayer(TestCase):
    def setUp(self):
        db.init(':memory:')
        classes = [Team, League, Season, PlayerStats, Person, Player]
        db.create_tables(classes)
        for class_ in classes:
            if class_.__name__ not in PMDataObject.deferred_relations:
                PMDataObject.deferred_relations[class_.__name__] = class_
        self.league = League.create(name="NHL")
        self.team = Team.create(name="Canucks",
                city="Vancouver",
                skill=100,
                abbreviation="VAN",
                league=self.league)
        self.person = Person.create_from_name(name=Name(forename = "Cliff",
            surname = "Ronning"))
        self.player = Player.create(person=self.person, team = self.team,
                position = "C", scoring_rate=0.07, shot_rate=6)

        self.season = Season.create(league=self.league,
                start_year=2016,
                end_year=2017,
                is_current=True)

    def test_creation(self):
        self.assertEqual(self.player.person.forename, "Cliff")
        self.assertEqual(self.player.person.surname, "Ronning")
        self.assertEqual(self.player.team, self.team)
        self.assertEqual(self.player.position, "C")
        self.assertEqual(self.player.scoring_rate, 0.07)
        self.assertEqual(self.player.shot_rate, 6)
        self.assertIsNotNone(self.player.id)

    def test_stats_creation(self):
        stats = self.player.current_team_season_stats()
        self.assertEqual(stats.player, self.player)

    def test_scored(self):
        self.player.scored(3)
        self.assertEqual(self.player.current_team_season_stats().goals, 3)

    def test_assisted(self):
        self.player.assisted(2)
        self.assertEqual(self.player.current_team_season_stats().assists, 2)
