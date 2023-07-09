#!/usr/bin/python3
""" test User model """
import unittest
from models.user import User


class BasemodelClass(unittest.TestCase):
    """test basemodel"""
    def test_UserEmail(self):
        inst = User()
        self.assertEqual(inst.email, '')
        self.assertEqual(inst.password, '')
        self.assertEqual(inst.first_name, '')
        self.assertEqual(inst.last_name, '')
