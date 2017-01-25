#!/usr/bin/env python
"""Unit tests for the PlayerStats class"""

from unittest import TestCase
from puckman.database import Database
from sqlalchemy.orm import sessionmaker
from puckman.models.player import Player
from puckman.models.stats.player import PlayerStats
from puckman.models.league import League
from puckman.models.season import Season
from puckman.models.team import Team


class TestPlayerStats(TestCase):
    def setUp(self):
        self.db = Database.new_db()
        Session = sessionmaker(bind=self.db.engine)
        self.session = Session()
        self.league = League(name="Band Battle")
        self.season = Season(league=self.league,
                start_year=2016,
                end_year=2017,
                is_current=True)

        self.team = Team(name="Sex Bob-omb", 
                city="Toronto", 
                abbreviation="TOR", 
                league=self.league)
        self.player = Player(
                forename="Scott",
                surname="Pilgrim",
                team=self.team,
                position="RW",
                scoring_rate=12.0,
                shot_rate=12.0,
                )
        self.stats = PlayerStats(player=self.player,
                season=self.season,
                team=self.team)
        self.session.add_all([
            self.league,
            self.season,
            self.team,
            self.player,
            self.stats])
        self.session.commit()

    def test_add_goals(self):
        self.stats.add_goals(3)
        self.assertEqual(self.stats.goals, 3)

    def test_add_assists(self):
        self.stats.add_assists(1)
        self.assertEqual(self.stats.assists, 1)
