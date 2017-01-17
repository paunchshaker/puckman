#!/usr/bin/env python
"""Unit tests for the Game class"""

from unittest import TestCase
from mock import Mock
from puckman.data_object import PMDataObject, db
from puckman.season import Season
from puckman.league import League
from puckman.team import Team
from puckman.stats.team import TeamStats
from puckman.game import Game

class TestGame(TestCase):
    def setUp(self):
        # TODO Lots of redundancy here with main app and other tests. Can we
        # abstract?
        db.init(':memory:')
        classes = PMDataObject.__subclasses__()
        db.create_tables(classes)
        for class_ in classes:
            if class_.__name__ not in PMDataObject.deferred_relations:
                PMDataObject.deferred_relations[class_.__name__] = class_
        league = League.create(name="Band Battle")
        season = Season.create(league=league,
                start_year=2016,
                end_year=2017,
                is_current=True)
        self.team1 = Team.create(name="Sex Bob-omb",
                city="Toronto",
                skill=90,
                abbreviation="SBO",
                league=league)
        TeamStats.create(team=self.team1, season=season)
        self.team2 = Team.create(name="The Clash at Demonhead",
                city="New York",
                skill=90,
                abbreviation="TCD",
                league=league)
        TeamStats.create(team=self.team2, season=season)
    
    def test_creation(self):
        game = Game(home = self.team1, visitor = self.team2)

        self.assertEqual(game.home, self.team1)
        self.assertEqual(game.visitor, self.team2)

    def test_simulate_scoring(self):
        self.team1.skill = 100
        self.team2.skill = 0
        game = Game(home = self.team1, visitor = self.team2)
        home, visitor = game.simulate_scoring(self.team1, self.team2)
        self.assertTrue(home > visitor)
    
        self.assertEqual(self.team1.current_season_stats().goals_for, home)
        self.assertEqual(self.team2.current_season_stats().goals_against, home)

    def test_update_team_records(self):
        game = Game(home = self.team1, visitor = self.team2)
        game.update_team_records(self.team1, 5, self.team2, 2)

        self.assertEqual(self.team1.current_season_stats().wins, 1)
        self.assertEqual(self.team2.current_season_stats().losses, 1)

        game.update_team_records(self.team1, 2, self.team2, 2)

        self.assertEqual(self.team1.current_season_stats().ties, 1)
        self.assertEqual(self.team2.current_season_stats().ties, 1)
