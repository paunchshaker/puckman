"""This module generates names"""

from numpy.random import choice
from puckman.name import Name
import puckman.census_name_generator as cng
from puckman.census_name_generator.surname_parser import SurnameParser
from puckman.census_name_generator.forename_parser import ForenameParser

class NameGenerator:

    """Generates names"""

    def __init__(self):
        """Load possible names"""
        surname_parser = SurnameParser(cng.surname_source)
        forename_parser = ForenameParser(cng.forename_source)
        self.first_names, self.first_name_freq = forename_parser.parse()
        self.last_names, self.last_name_freq = surname_parser.parse()

    def generate(self):
        """Generate a random name"""
        return Name(forename=choice(self.first_names, p=self.first_name_freq),
                surname=choice(self.last_names, p=self.last_name_freq))

