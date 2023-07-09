#!/usr/bin/python3
""" test Amenity model """
import unittest
from models.amenity import Amenity


class BasemodelClass(unittest.TestCase):
    """test basemodel"""
    def test_amenity(self):
        """tests"""
        inst = Amenity()
        self.assertEqual(inst.name, "")

