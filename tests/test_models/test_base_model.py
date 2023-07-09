#!/usr/bin/python3
"""Unittest for class BaseModel methods"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pickle


class Test_classBasemodel(unittest.TestCase):
    """class that incliude all class"""

    def test_attr_types(self):
        """check the types of the class atributes"""
        base0 = BaseModel()

        self.assertEqual(type(base0.id), str)
        self.assertEqual(type(base0.created_at), datetime)

    def test_to_dict(self):
        """ check the correct convention of all atriutes of an instance /
        into a dictionary"""
        base1 = BaseModel()
        new_dict = base1.to_dict()

        self.assertEqual(type(new_dict), dict)
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)

    def test_str(self):
        model = BaseModel()
        prinf = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(prinf, model.__str__())

    def test_save(self):
        my_model = BaseModel()
        try:
            os.remove("file.pkl")
        except Exception:
            pass

        with open("file.pkl", "wb") as file:
            pickle.dump(my_model, file)

        self.assertTrue(os.path.exists("file.pkl"))


