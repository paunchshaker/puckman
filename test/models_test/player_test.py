#!/usr/bin/env python
"""Unit tests for the Player class"""

from unittest import TestCase
from puckman.database import Database
from sqlalchemy.orm import sessionmaker
from puckman.models.league import League
from puckman.models.team import Team
from puckman.models.person import Person
from puckman.models.player import Player
from puckman.name import Name
from puckman.models.season import Season
from puckman.models.stats.player import PlayerStats

class TestPlayer(TestCase):
    def setUp(self):
        self.db = Database.new_db()
        Session = sessionmaker(bind=self.db.engine)
        self.session = Session()
        self.league = League(name="NHL")
        self.team = Team(name="Canucks",
                city="Vancouver",
                abbreviation="VAN",
                league=self.league)
        self.player = Player(
                name=Name(forename = "Cliff", surname = "Ronning"),
                team = self.team,
                position = "C",
                scoring_rate=0.07,
                shot_rate=6)

        self.season = Season(league=self.league,
                start_year=2016,
                end_year=2017,
                is_current=True)
        self.session.add_all([
                self.league,
                self.team,
                self.player,
                self.season])
        self.session.commit()


    def test_creation(self):
        self.assertEqual(self.player.name.forename, "Cliff")
        self.assertEqual(self.player.name.surname, "Ronning")
        self.assertEqual(self.player.team, self.team)
        self.assertEqual(self.player.position, "C")
        self.assertEqual(self.player.scoring_rate, 0.07)
        self.assertEqual(self.player.shot_rate, 6)
        self.assertIsNotNone(self.player.id)

    def test_stats_creation(self):
        stats = self.player.current_team_season_stats()
        self.assertEqual(stats.player, self.player)

    def test_scored(self):
        self.session.add(self.player.current_team_season_stats())
        self.session.commit()
        self.player.scored(3)
        self.assertEqual(self.player.current_team_season_stats().goals, 3)

    def test_assisted(self):
        self.session.add(self.player.current_team_season_stats())
        self.session.commit()
        self.player.assisted(2)
        self.assertEqual(self.player.current_team_season_stats().assists, 2)
