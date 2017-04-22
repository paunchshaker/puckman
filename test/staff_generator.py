#!/usr/bin/env python
"""Unit tests for the StaffGenerator class"""

from unittest import TestCase
from mock import Mock
from puckman.models.staff import Staff
from puckman.staff_generator import StaffGenerator

class TestStaffGenerator(TestCase):
    def test_creation(self):
        generator = StaffGenerator()
        self.assertIsNotNone(generator)
        random_staffer = generator.generate()
        self.assertIsNotNone(random_staffer)
        self.assertIsNotNone(random_staffer.name)
        self.assertIsNotNone(random_staffer.job)
