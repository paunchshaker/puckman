#!/usr/bin/env python

import random
from flask import Flask, redirect, url_for, render_template
from puckman.league import League
from puckman.team import Team
from puckman.record import Record
from puckman.game import Game
from puckman.player_generator import PlayerGenerator

app = Flask(__name__)

@app.route('/')
def index():
    """the main screen for the game"""
    return render_template("index.html", teams = sorted(app.league.teams, key=lambda team: team.record.wins * 2, reverse=True))

def create_test_league():
    """This method creates a junk league for demo purposes"""
    team1 = Team(name = "Komets", city = "Fort Wayne", skill = 90, record = Record(), abbreviation = "FTW")
    team2 = Team(name = "Ice", city = "Indianapolis", skill = 80, record = Record(), abbreviation = "IND")
    team3 = Team(name = "Aeros", city = "Houston", skill = 70, record = Record(), abbreviation = "HOU")
    team4 = Team(name = "Whoopie", city = "Macon", skill = 75, record = Record(), abbreviation = "MAC")

    return League(name="Fake League", teams=[team1, team2, team3, team4])

def add_players(number, league):
    """Generate random players and adds to the league"""
    generator = PlayerGenerator()
    i = 0
    while i < number:
        player = generator.generate()
        league.roster.add_player(player)
        i += 1

@app.route('/action/sim_season')
def sim_season():
    i = 0
    for team in app.league.teams:
        team.record = Record()
    while i < 82:
        matchups = app.league.teams
        random.shuffle(matchups)
        for home, visitor in [(matchups[0], matchups[1]), (matchups[2], matchups[3])]:
            game = Game(home = home, visitor = visitor)
            game.play()
        i += 1
    return redirect(url_for('index'))

@app.route('/players')
def list_players():
    """Lists all players in the league universe"""
    return render_template("player_view.html", players = app.league.roster.players())

@app.route('/player_card/<player_uuid>')
def show_player_card(player_uuid):
    """Shows player card for a player"""
    player = None
    for p in app.league.roster.players():
        if p.id() == player_uuid:
            player = p
    return render_template("player_card.html", player = player)

if __name__ == '__main__':
    app.league = create_test_league()
    add_players(25, app.league)
    app.run(debug = True)
