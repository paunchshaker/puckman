#!/usr/bin/env python

import random
from puckman.league import League
from puckman.team import Team
from puckman.record import Record

def main():
    """the game"""

    team1 = Team(name = "Komets", city = "Fort Wayne", skill = 90, record = Record())
    team2 = Team(name = "Ice", city = "Indianapolis", skill = 80, record = Record())
    team3 = Team(name = "Aeros", city = "Houston", skill = 70, record = Record())
    team4 = Team(name = "Whoopie", city = "Macon", skill = 75, record = Record())

    league = League(name="Fake League", teams=[team1, team2, team3, team4])
    while 1:
        command = input("Press enter for next turn, type p to print standings, or type q to end: ")
        command = command.strip().lower()
        if command == "p":
            print(str(league))
            input()
        elif command == "q":
            break
        else:
            matchups = league.teams
            random.shuffle(matchups)
            for home, visitor in [(matchups[0], matchups[1]), (matchups[2], matchups[3])]:
                cutoff = (home.skill-visitor.skill)/100 + 0.5
                if(random.uniform(0, 1) < cutoff):
                    home.won()
                    visitor.lost()
                else:
                    home.lost()
                    visitor.won()


if __name__ == '__main__':
    main()
