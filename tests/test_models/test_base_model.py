#!/usr/bin/python3
"""
Unittest for class BaseModel methods
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
import os
import pickle


class BaseModelClass(unittest.TestCase):
    """ Test basemodel """
    def test_save(self):
        inst = BaseModel()
        cr = inst.created_at
        up = inst.updated_at
        inst.save()
        self.assertEqual(cr, inst.created_at)
        self.assertNotEqual(up, inst.updated_at)

    def test_to_dict(self):
        inst = BaseModel()
        d = {key: value for key, value in inst.__dict__.items()}
        d['__class__'] = inst.__class__.__name__
        d['created_at'] = inst.created_at.isoformat("T")
        d['updated_at'] = inst.updated_at.isoformat("T")
        self.assertEqual(d, inst.to_dict())

    def test_string(self):
        inst = BaseModel()
        self.assertEqual(str, type(str(inst)))
        s = f'[{inst.__class__.__name__}] ({inst.id}) {inst.__dict__}'
        self.assertEqual(s, str(inst))
    
    def test_save(self):
        b = BaseModel()
        try:
            os.remove('file.json')
        except Exception:
            pass
        b.save()
        self.assertTrue(os.path.exists('file.json'))
