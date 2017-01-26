#!/usr/bin/env python
"""Unit tests for the Game class"""

from unittest import TestCase
from puckman.database import Database
from sqlalchemy.orm import sessionmaker
from puckman.models.season import Season
from puckman.models.league import League
from puckman.models.team import Team
from puckman.models.stats.team import TeamStats
from puckman.game import Game

class TestGame(TestCase):
    def setUp(self):
        self.db = Database.new_db()
        Session = sessionmaker(bind=self.db.engine)
        self.session = Session()
        self.league = League(name="Band Battle")
        self.season = Season(league=self.league,
                start_year=2016,
                end_year=2017,
                is_current=True)
        self.team1 = Team(name="Sex Bob-omb",
                city="Toronto",
                abbreviation="SBO",
                league=self.league)
        self.team1_stats = TeamStats(team=self.team1, season=self.season)
        self.team2 = Team(name="The Clash at Demonhead",
                city="New York",
                abbreviation="TCD",
                league=self.league)
        self.team2_stats = TeamStats(team=self.team2, season=self.season)
        self.session.add_all([
            self.league,
            self.season,
            self.team1,
            self.team1_stats,
            self.team2,
            self.team2_stats])
        self.session.commit()
    
    def test_creation(self):
        game = Game(home = self.team1, visitor = self.team2)

        self.assertEqual(game.home, self.team1)
        self.assertEqual(game.visitor, self.team2)
