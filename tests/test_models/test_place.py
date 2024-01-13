#!/usr/bin/python3
""" unit test for Review """
import unittest
from models.place import Place
from datetime import datetime


class PlaceTestCase(unittest.TestCase):
    """ class for place test """

    def test_place(self):
        """existince"""
        pl = Place()
        self.assertTrue(hasattr(pl, "id"))
        self.assertTrue(hasattr(pl, "created_at"))
        self.assertTrue(hasattr(pl, "updated_at"))
        self.assertTrue(hasattr(pl, "city_id"))
        self.assertTrue(hasattr(pl, "user_id"))
        self.assertTrue(hasattr(pl, "name"))
        self.assertTrue(hasattr(pl, "description"))
        self.assertTrue(hasattr(pl, "number_rooms"))
        self.assertTrue(hasattr(pl, "number_bathrooms"))
        self.assertTrue(hasattr(pl, "max_guest"))
        self.assertTrue(hasattr(pl, "price_by_night"))
        self.assertTrue(hasattr(pl, "latitude"))
        self.assertTrue(hasattr(pl, "longitude"))
        self.assertTrue(hasattr(pl, "amenity_ids"))

        """type test"""
        self.assertIsInstance(pl.id, str)
        self.assertIsInstance(pl.created_at, datetime)
        self.assertIsInstance(pl.updated_at, datetime)
        self.assertIsInstance(pl.city_id, str)
        self.assertIsInstance(pl.user_id, str)
        self.assertIsInstance(pl.name, str)
        self.assertIsInstance(pl.description, str)
        self.assertIsInstance(pl.number_rooms, int)
        self.assertIsInstance(pl.number_bathrooms, int)
        self.assertIsInstance(pl.max_guest, int)
        self.assertIsInstance(pl.price_by_night, int)
        self.assertIsInstance(pl.latitude, float)
        self.assertIsInstance(pl.longitude, float)
        self.assertIsInstance(pl.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
