#!/usr/bin/python3
""" test State model """
import unittest
from models.state import State

class BasemodelClass(unittest.TestCase):
    """test basemodel"""
    def test_review(self):
        inst = State()
        self.assertEquals(inst.name, '')
