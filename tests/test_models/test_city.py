#!/usr/bin/python3
""" test City model """
import unittest
from models.city import City


class BasemodelClass(unittest.TestCase):
    """test basemodel"""
    def test_city(self):
        inst = City()
        self.assertEqual(inst.name, '')
        self.assertEqual(inst.state_id, '')


if __name__ == '__main__':
    unittest.main()
