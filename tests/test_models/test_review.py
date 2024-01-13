#!/usr/bin/python3
"""unit test for review"""
import unittest
from models.review import Review
from datetime import datetime

class ReviewTestCase(unittest.TestCase):
    """class for review test"""
    def test_review(self):
        """existince"""
        rv = Review()
        self.assertTrue(hasattr(rv, "id"))
        self.assertTrue(hasattr(rv, "created_at"))
        self.assertTrue(hasattr(rv, "updated_at"))
        self.assertTrue(hasattr(rv, "place_id"))
        self.assertTrue(hasattr(rv, "user_id"))
        self.assertTrue(hasattr(rv, "text"))

        """type test"""
        self.assertIsInstance(rv.id, str)
        self.assertIsInstance(rv.created_at, datetime)
        self.assertIsInstance(rv.updated_at, datetime)
        self.assertIsInstance(rv.place_id, str)
        self.assertIsInstance(rv.user_id, str)
        self.assertIsInstance(rv.text, str)
        