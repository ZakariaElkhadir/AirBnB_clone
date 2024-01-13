#!/usr/bin/python3
""" unit test for City """
import unittest
from models.city import City
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ class for city test """

    def test_city(self):
        """existince"""
        ci = City()
        self.assertTrue(hasattr(ci, "id"))
        self.assertTrue(hasattr(ci, "created_at"))
        self.assertTrue(hasattr(ci, "updated_at"))
        self.assertTrue(hasattr(ci, "state_id"))
        self.assertTrue(hasattr(ci, "name"))

        """type test"""
        self.assertIsInstance(ci.id, str)
        self.assertIsInstance(ci.created_at, datetime)
        self.assertIsInstance(ci.updated_at, datetime)
        self.assertIsInstance(ci.state_id, str)
        self.assertIsInstance(ci.name, str)


if __name__ == '__main__':
    unittest.main()
