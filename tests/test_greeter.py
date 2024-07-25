# tests/test_greeter.py

import unittest
from app.greeter import greet, farewell

class TestGreeter(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_farewell(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")
        self.assertEqual(farewell("Bob"), "Goodbye, Bob!")

if __name__ == '__main__':
    unittest.main()
