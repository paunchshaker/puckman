#!/usr/bin/env python
"""Unit tests for the PMDataObject class"""

from unittest import TestCase
from puckman.data_object import PMDataObject
from puckman.data_object import db

class TestPMDataObject(TestCase):
    def setUp(self):
        db.init(':memory:')
        db.create_tables([ PMDataObject ])
        self.data_object = PMDataObject()
        self.data_object.save()

    def test_creation(self):
        self.assertIsNotNone(self.data_object.id)
