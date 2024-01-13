#!/usr/bin/python3
"""unit test for state"""


import unittest
from models.state import State
from datetime import datetime


class StateTestCase(unittest.TestCase):
    """state test class"""
    def test_state(self):

        """existince"""
        self.assertTrue(hasattr(State(), "id"))
        self.assertTrue(hasattr(State(), "created_at"))
        self.assertTrue(hasattr(State(), "updated_at"))
        self.assertTrue(hasattr(State(), "name"))
        """type test"""

        self.assertIsInstance(State().id, str)
        self.assertIsInstance(State().created_at, datetime)
        self.assertIsInstance(State().updated_at, datetime)
        self.assertIsInstance(State().name, str)


if __name__ == "__main__":
    unittest.main()
