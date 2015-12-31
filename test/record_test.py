#!/usr/bin/env python
"""Unit tests for the Record class"""

from unittest import TestCase
from mock import Mock
from puckman.record import Record

class TestRecord(TestCase):
    def test_creation_with_no_args(self):
        record = Record()
        self.assertEqual(record.wins,0)
        self.assertEqual(record.losses,0)
        self.assertEqual(record.ties,0)
    def test_creation_with_args(self):
        record = Record(1,2)
        self.assertEqual(record.wins,1)
        self.assertEqual(record.losses,2)
    def test_add_win(self):
        record = Record()
        record.add_win()
        self.assertEqual(record.wins, 1)
    def test_add_loss(self):
        record = Record()
        record.add_loss()
        self.assertEqual(record.losses, 1)
    def test_add_tie(self):
        record = Record()
        record.add_tie()
        self.assertEqual(record.ties, 1)
    def test_equality_overload(self):
        record1 = Record(1,1,1)
        record2 = Record(1,1,1)
        self.assertEqual(record1, record2)
    def test_inequality_overload(self):
        record1 = Record(1,2)
        record2 = Record(1,1)
        self.assertNotEqual(record1, record2)
        record1 = Record(1,1,1)
        record2 = Record(1,1)
        self.assertNotEqual(record1, record2)

