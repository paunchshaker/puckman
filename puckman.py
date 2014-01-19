#!/usr/bin/env python

import random
from puckman.league import League
from puckman.team import Team
from puckman.record import Record
from puckman.game import Game

def main():
    """the game"""

    team1 = Team(name = "Komets", city = "Fort Wayne", skill = 90, record = Record(), abbreviation = "FTW")
    team2 = Team(name = "Ice", city = "Indianapolis", skill = 80, record = Record(), abbreviation = "IND")
    team3 = Team(name = "Aeros", city = "Houston", skill = 70, record = Record(), abbreviation = "HOU")
    team4 = Team(name = "Whoopie", city = "Macon", skill = 75, record = Record(), abbreviation = "MAC")

    league = League(name="Fake League", teams=[team1, team2, team3, team4])
    while 1:
        command = input("Press enter for next turn, type p to print standings, or type q to end: ")
        command = command.strip().lower()
        if command == "p":
            print(str(league))
        elif command == "q":
            break
        else:
            matchups = league.teams
            random.shuffle(matchups)
            for home, visitor in [(matchups[0], matchups[1]), (matchups[2], matchups[3])]:
                game = Game(home = home, visitor = visitor)
                game.play()

if __name__ == '__main__':
    main()
