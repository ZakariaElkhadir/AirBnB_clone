#!/usr/bin/python3
""" unit test for Amenity """
import unittest
from models.amenity import Amenity
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ class for amenity test """

    def test_amenity(self):
        """existince"""
        am = Amenity()
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))
        self.assertTrue(hasattr(am, "name"))

        """type test"""
        self.assertIsInstance(am.id, str)
        self.assertIsInstance(am.created_at, datetime)
        self.assertIsInstance(am.updated_at, datetime)
        self.assertIsInstance(am.name, str)


if __name__ == '__main__':
    unittest.main()
