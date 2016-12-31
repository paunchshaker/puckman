"""This parses a file of surnames into two lists: one of names and one of their
expected frequency"""

import csv

class SurnameParser:

    """Reads in surnames from file"""

    def __init__(self, file_name):
        """Loads possible surnames and their frequencies from a file"""
        self.file_name = file_name

    def parse(self):
        names = list()
        frequencies = list()
        with open(self.file_name) as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                name = row['name'].title()
                names.append(name)
                freq = float(row['prop100k'])/100000
                frequencies.append(freq)
        frequency_sum = sum(frequencies)
        freq_normalized = [ x / frequency_sum for x in frequencies]
        return names, freq_normalized
