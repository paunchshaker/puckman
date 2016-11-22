#!/usr/bin/env python
"""Unit tests for the TeamStats class"""

from puckman.data_object import db, PMDataObject
from puckman.stats.team import TeamStats
from puckman.league import League
from puckman.season import Season
from puckman.team import Team

from peewee import *
from unittest import TestCase

class TestTeamStats(TestCase):
    def setUp(self):
        db.init(':memory:')
        classes = [Team, League, Season, TeamStats]
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

        self.team_stats = TeamStats.create(team=self.team,
                season=self.season)

    def test_add_win(self):
        self.team_stats.add_win()
        self.assertEqual(self.team_stats.wins, 1)

    def test_add_loss(self):
        self.team_stats.add_loss()
        self.assertEqual(self.team_stats.losses, 1)

    def test_add_tie(self):
        self.team_stats.add_tie()
        self.assertEqual(self.team_stats.ties, 1)

    def test_add_goals_for(self):
        self.team_stats.add_goals_for(2)
        self.assertEqual(self.team_stats.goals_for, 2)

    def test_add_goals_against(self):
        self.team_stats.add_goals_against(3)
        self.assertEqual(self.team_stats.goals_against, 3)
