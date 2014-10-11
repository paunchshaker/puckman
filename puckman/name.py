"""This module contains code to handle names"""

class Name:
    """The Name class handles manipulations of personal names"""

    def __init__(self, forename, surname):
        """Initialize name"""
        self.forename = forename
        self.surname = surname

    def full_name(self):
        """Display full name in order"""
        return " ".join((self.forename, self.surname))

    def first_name(self):
        """First name"""
        return self.forename

    def last_name(self):
        """Last name"""
        return self.surname

    def lexical_name(self):
        """Name to display in alphabetical ordered lists"""
        return ", ".join((self.surname, self.forename))
