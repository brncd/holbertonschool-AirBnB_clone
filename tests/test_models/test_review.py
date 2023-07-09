#!/usr/bin/python3
""" test Review model """
import unittest
from models.review import Review


class BasemodelClass(unittest.TestCase):
    """test basemodel"""
    def test_review(self):
        inst = Review()
        self.assertEquals(inst.place_id, '')
        self.assertEquals(inst.user_id, '')
        self.assertEquals(inst.text, '')
