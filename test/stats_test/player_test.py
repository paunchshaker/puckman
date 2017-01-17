#!/usr/bin/env python
"""Unit tests for the PlayerStats class"""

from puckman.data_object import db, PMDataObject
from puckman.player import Player
from puckman.person import Person
from puckman.stats.player import PlayerStats
from puckman.league import League
from puckman.season import Season
from puckman.team import Team

from peewee import *
from unittest import TestCase

class TestPlayerStats(TestCase):
    def setUp(self):
        db.init(':memory:')
        classes = [Team, League, Season, Person, Player, PlayerStats]
        db.create_tables(classes)
        for class_ in classes:
            if class_.__name__ not in PMDataObject.deferred_relations:
                PMDataObject.deferred_relations[class_.__name__] = class_
        
        self.league = League.create(name="Band Battle")
        self.season = Season.create(league=self.league,
                start_year=2016,
                end_year=2017,
                is_current=True)

        self.team = Team.create(name="Sex Bob-omb", 
                city="Toronto", 
                skill=90,
                abbreviation="TOR", 
                league=self.league)
        self.person = Person.create(forename="Scott", surname="Pilgrim")
        self.player = Player.create(person=self.person,
                team=self.team,
                position="F",
                scoring_rate=12.0,
                shot_rate=12.0,
                )
        self.stats = PlayerStats.create(player=self.player,
                season=self.season,
                team=self.team)

    def test_add_goals(self):
        self.stats.add_goals(3)
        self.assertEqual(self.stats.goals, 3)

    def test_add_assists(self):
        self.stats.add_assists(1)
        self.assertEqual(self.stats.assists, 1)
