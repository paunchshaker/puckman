#!/usr/bin/env python
"""Unit tests for the PMDataObject class"""

from unittest import TestCase
from puckman.data_object import PMDataObject

class TestPMDataObject(TestCase):
    def setUp(self):
        self.data_object = PMDataObject()

    def test_creation(self):
        self.assertIsNotNone(self.data_object.uuid)
    def test_id(self):
        self.assertEqual(self.data_object.uuid.hex, self.data_object.id())
