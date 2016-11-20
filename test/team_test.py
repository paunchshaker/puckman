#!/usr/bin/env python
"""Unit tests for the Team class"""

from peewee import *
from unittest import TestCase
from mock import Mock
from puckman.data_object import db
from puckman.team import Team
from puckman.league import League
from puckman.season import Season
from puckman.stats.team import TeamStats

class TestTeam(TestCase):
    def setUp(self):
        db.init(':memory:')
        db.create_tables([Team, League, Season, TeamStats])
        
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
    
    def test_creation(self):
        self.assertEqual(self.team.league, self.league)
        self.assertEqual(self.team.name, "Sex Bob-omb")
        self.assertEqual(self.team.city, "Toronto")
        self.assertEqual(self.team.skill, 90)
        self.assertEqual(self.team.abbreviation, "TOR")
        self.assertIsNotNone(self.team.id)

    def test_bad_abbreviation(self):
        with self.assertRaises(IntegrityError):
            Team.create(name = "The Clash at Demonhead", city = "New York", skill = 50, abbreviation = "T")

    def test_current_season_stats(self):
        self.assertEqual(self.team.current_season_stats().id,
                self.team_stats.id)
    
    def test_win(self):
        self.team.won()
        self.assertEqual(self.team.current_season_stats().wins, 1)

    def test_loss(self):
        self.team.lost()
        self.assertEqual(self.team.current_season_stats().losses, 1)

    def test_tied(self):
        self.team.tied()
        self.assertEqual(self.team.current_season_stats().ties, 1)

    def test_register_results(self):
        self.team.register_result(5, 2)
        self.assertEqual(self.team.current_season_stats().goals_for, 5)
        self.assertEqual(self.team.current_season_stats().goals_against, 2)
