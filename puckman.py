#!/usr/bin/env python

import random
from flask import Flask, redirect, url_for, render_template
from puckman.league import League
from puckman.season import Season
from puckman.team import Team
from puckman.stats.team import TeamStats
from puckman.game import Game
from puckman.player_generator import PlayerGenerator
from puckman.player import Player
import puckman.data_object

app = Flask(__name__)

@app.route('/')
def index():
    """the main screen for the game"""
    teams = app.league.teams
    ranked_teams = sorted(app.league.teams, key=lambda x: x.current_season_stats().wins * 2 + x.current_season_stats().ties, reverse=True)
    return render_template("index.html", teams=ranked_teams)

def create_test_league():
    """This method creates a junk league for demo purposes"""
    main_league = League.create(name="Fake League")
    Team.create(league=main_league, name = "Komets", city = "Fort Wayne", skill = 2.5, abbreviation = "FTW")
    Team.create(league=main_league, name = "Ice", city = "Indianapolis", skill = 2.4, abbreviation = "IND")
    Team.create(league=main_league, name = "Aeros", city = "Houston", skill = 2.3, abbreviation = "HOU")
    Team.create(league=main_league, name = "Whoopie", city = "Macon", skill = 2.1, abbreviation = "MAC")
    new_season(main_league)

    return main_league

def add_players(number, league):
    """Generate random players and adds to the league"""
    generator = PlayerGenerator()
    i = 0
    while i < number:
        player = generator.generate()
        i += 1

def draft_players(league):
    """Assign players to teams at random"""
    teams = list(league.teams)
    for player in Player.select():
        team = random.choice(teams)
        player.team = team
        player.save()

def new_season(league):
    old_season = league.current_season
    if old_season is None:
        new_season = Season.create(league=league,
                start_year=2016,
                end_year=2017,
                is_current=True)
    else:
        old_season.is_current = False
        old_season.save()
        new_season = Season.create(league=league,
                start_year=old_season.start_year + 1,
                end_year=old_season.end_year + 1,
                is_current=True)
    for team in league.teams:
        TeamStats.create(team=team, season=new_season)

@app.route('/action/sim_season')
def sim_season():
    if app.first:
        app.first = False
    else:
        new_season(app.league)
    matchups = list(app.league.teams)
    i = 0
    while i < 82:
        random.shuffle(matchups)
        for home, visitor in [(matchups[0], matchups[1]), (matchups[2], matchups[3])]:
            game = Game(home=home, visitor=visitor)
            game.play()
        i += 1
    return redirect(url_for('index'))

@app.route('/players')
def list_players():
    """Lists all players in the league universe"""
    return render_template("player_view.html", players = Player.select())

@app.route('/player_card/<player_id>')
def show_player_card(player_id):
    """Shows player card for a player"""
    player = Player.get(Player.id == player_id)
    return render_template("player_card.html", player=player)

@app.route('/team_page/<team_id>')
def show_team_page(team_id):
    """Shows Team information"""
    team = Team.select().where(Team.id == team_id).get()
    return render_template("team_page.html", team=team)

if __name__ == '__main__':
    # initialize database
    db = puckman.data_object.db
    db.init(':memory:')
    classes = puckman.data_object.PMDataObject.__subclasses__()
    db.create_tables(classes)
    for class_ in classes:
        if class_.__name__ not in puckman.data_object.PMDataObject.deferred_relations:
             puckman.data_object.PMDataObject.deferred_relations[class_.__name__] = class_
    
    app.league = create_test_league()
    app.first = True
    add_players(100, app.league)
    draft_players(app.league)
    app.run(debug = True, use_reloader=False)
