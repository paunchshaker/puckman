"""This module contains code describing the record of a team"""

class Record:

    """The Record class defines information about a team's win/loss record"""

    def __init__(self, wins=0, losses=0, ties=0):
        """Initializes a new Record."""
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.__hash__ = None

    def __eq__(self, other):
        return self.wins == other.wins and self.losses == other.losses and self.ties == other.ties

    def __ne__(self, other):
        return not self.__eq__(other)

    def add_win(self):
        """Add a win to the record."""
        self.wins += 1

    def add_loss(self):
        """Add a loss to the record."""
        self.losses += 1

    def add_tie(self):
        """Add a tie to the record."""
        self.ties += 1

