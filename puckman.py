#!/usr/bin/env python

from puckman.models.league import League
from puckman.models.season import Season
from puckman.models.team import Team
from puckman.models.stats.team import TeamStats
from puckman.game import Game
from puckman.player_generator import PlayerGenerator
from puckman.models.player import Player
from puckman.models.stats.player import PlayerStats
from puckman.database import Database

import os
import random
from itertools import cycle
from flask import Flask, redirect, url_for, render_template, request, jsonify
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route('/')
def splash_screen():
    return render_template("splash.html")

@app.route('/main')
def index():
    """the main screen for the game"""
    ranked_teams = sorted(app.league.teams, key=lambda x: x.current_season_stats().wins * 2 + x.current_season_stats().ties, reverse=True)
    top_scorers = [x[0] for x in app.session.query(PlayerStats, Season).filter(PlayerStats.season_id == Season.id).filter(Season.is_current == True).filter(Season.league == app.league).all()]
    top_scorers = sorted(top_scorers, key=lambda x: x.goals + x.assists, reverse=True)[:10]
    goalies = app.session.query(Player.id).filter(Player.position == 'G').subquery()
    goalie_stats = list(app.session.query(PlayerStats, Season).filter(PlayerStats.season_id == Season.id).filter(Season.is_current == True).filter(Season.league == app.league).filter(PlayerStats.player_id.in_(goalies)).all())
    return render_template("index.html", teams=ranked_teams, top_scorers=top_scorers, top_goalies=[x[0] for x in goalie_stats])

def create_test_league():
    """This method creates a junk league for demo purposes"""
    main_league = League(name="Fake League")
    app.session.add(main_league)
    app.session.add(Team(league=main_league, name = "Komets", city = "Fort Wayne", abbreviation = "FTW"))
    app.session.add(Team(league=main_league, name = "Ice", city = "Indianapolis", abbreviation = "IND"))
    app.session.add(Team(league=main_league, name = "Aeros", city = "Houston", abbreviation = "HOU"))
    app.session.add(Team(league=main_league, name = "Whoopie", city = "Macon", abbreviation = "MAC"))
    new_season(main_league)
    app.session.commit()

    return main_league

@app.route('/draft')
def draft():
    """Assign players to teams via draft"""
    teams = list(app.league.teams)
    players = app.session.query(Player).filter(Player.team == None).all()
    if not players:
        app.drafting_team = None
        return redirect(url_for('index'))

    if app.drafting_team is None:
        random.shuffle(teams)
        app.drafting_team = cycle(teams)
    current_team = next(app.drafting_team)
    while current_team.name != 'Ice' and players:
        drafted_player = random.choice(players)
        players.remove(drafted_player)
        _draft_player(drafted_player, current_team)
        current_team = next(app.drafting_team)

    return render_template("draft.html", players=players, team=current_team, draft_name="Fantasy Draft")

def add_players(number):
    """Generate random players and adds to the league"""
    generator = PlayerGenerator()
    i = 0
    while i < number:
        new_player = generator.generate()
        app.session.add(new_player)
        i += 1

def new_season(league):
    """Start a new season"""
    old_season = league.current_season
    if old_season is None:
        new_season = Season(league=league,
                start_year=2016,
                end_year=2017,
                is_current=True)
        app.session.add(new_season)
    else:
        old_season.is_current = False
        app.session.add(old_season)
        new_season = Season(league=league,
                start_year=old_season.start_year + 1,
                end_year=old_season.end_year + 1,
                is_current=True)
        app.session.add(new_season)
    for team in league.teams:
        new_stat = TeamStats(team=team, season=new_season)
        app.session.add(new_stat)
    app.session.commit()

@app.route('/action/sim_season')
def sim_season():
    """Simulate a full season"""
    if app.first:
        app.first = False
    else:
        new_season(app.league)
    matchups = list(app.league.teams)
    i = 0
    while i < 82:
        random.shuffle(matchups)
        for home, visitor in [(matchups[0], matchups[1]), (matchups[2], matchups[3])]:
            game = Game(home=home, visitor=visitor, session=app.session)
            game.play()
        i += 1
    finalize_season(app.league.teams)
    app.session.commit()
    return redirect(url_for('index'))

def finalize_season(teams):
    ranked_teams = sorted(teams, key=lambda x: x.current_season_stats().wins * 2 + x.current_season_stats().ties, reverse=True)
    for rank, team in enumerate(ranked_teams):
        stats = team.current_season_stats()
        stats.rank = rank + 1

@app.route('/action/draft_player', methods=['POST'])
def draft_player():
    """Draft player to a team"""
    if request.method == 'POST':
        player = app.session.query(Player).get(request.form['player_id'])
        team = app.session.query(Team).get(request.form['team_id'])
        _draft_player(player, team)
        return '', 204

def _draft_player(player, team):
        player.team = team
        app.session.commit()
        print("{2} {0} drafted by {1}\n".format(player.full_name(), team.name, player.position))


@app.route('/players')
def list_players():
    """Lists all players in the league universe"""
    return render_template("player_view.html", players =
            app.session.query(Player).all())

@app.route('/player_card/<player_id>')
def show_player_card(player_id):
    """Shows player card for a player"""
    player = app.session.query(Player).get(player_id)
    return render_template("player_card.html", player=player)

@app.route('/team_page/<team_id>')
def show_team_page(team_id):
    """Shows Team information"""
    team = app.session.query(Team).get(team_id)
    stats = list(team.stats)
    roster = list(team.roster)
    return render_template("team_page.html", team=team, roster=roster, stats=stats)

@app.route('/action/new_game')
def new_game():
    # initialize database
    if os.path.exists('foo.db'):
        os.remove('foo.db')
    app.db = Database.new_db('foo.db')
    Session = sessionmaker(bind=app.db.engine)
    # For now try using one session for the whole application
    app.session = Session()

    app.drafting_team = None
    app.league = create_test_league()
    app.first = True
    add_players(100)
    return redirect(url_for('index'))

@app.route('/action/load_game')
def load_game():
    app.db = Database.load_db('foo.db')
    Session = sessionmaker(bind=app.db.engine)
    # For now try using one session for the whole application
    app.session = Session()
    app.league = app.session.query(League).get(1) #only 1 league so just grab it
    app.first = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True, use_reloader=False)
