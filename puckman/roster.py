"""Abstraction to handle tracking a team's roster"""

class Roster:
    """Track and enforce restrictions for players assigned to a team's playing roster"""

    def __init__(self):
        """Initialize a new Roster."""
        self._players = set()

    def add_player(self, player):
        """Add a player to the roster"""
        self._players.add(player)

    def remove_player(self, player):
        """Remove a player from the roster"""
        self._players.remove(player)

    def players(self):
        return list(self._players)
