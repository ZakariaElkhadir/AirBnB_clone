#!/usr/bin/python3
"""unit test for user"""
import unittest
from models.user import User
from datetime import datetime


class UserTestCase(unittest.TestCase):
    """class for user test"""
    def test_user(self):
        """existince"""
        pl = User()
        self.assertTrue(hasattr(pl, "id"))
        self.assertTrue(hasattr(pl, "created_at"))
        self.assertTrue(hasattr(pl, "updated_at"))
        self.assertTrue(hasattr(pl, "email"))
        self.assertTrue(hasattr(pl, "password"))
        self.assertTrue(hasattr(pl, "first_name"))
        self.assertTrue(hasattr(pl, "last_name"))

        """type test"""
        self.assertIsInstance(pl.id, str)
        self.assertIsInstance(pl.created_at, datetime)
        self.assertIsInstance(pl.updated_at, datetime)
        self.assertIsInstance(pl.email, str)
        self.assertIsInstance(pl.password, str)
        self.assertIsInstance(pl.first_name, str)
        self.assertIsInstance(pl.last_name, str)

if __name__ == "__main__":
    unittest.main()
