#!/usr/bin/python3
""" file storage tests """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FilestorageClass(unittest.TestCase):
    """test file storage"""
    def test_filepath(self):
        """file path is set on file.json"""
        inst = FileStorage()

    def test_objects(self):
        """check privat atribute __objects"""
        inst = FileStorage()
        self.assertEqual(type(inst._Filestorage__objects), dict)

    def test_all(self):
        inst = BaseModel
        self.assertEqual(type(inst.all()), dict)
    
    def test_new(self):
        model = BaseModel()
        inst = FileStorage()
        inst.new(model)
        prin = f"{model.__class__.__name__}.{model.id}"
        self.assertEqual(inst.all()[prin], model)

    def test_save(self):
        model = FileStorage()
        model.all().clear()
        inst = BaseModel()
        model.save()
        self.assertNotEqual(len(model.all()), 0)

    def test_reload(self):
        inst = FileStorage()
        inst.all().clear()
        inst.save()
        self.assertNotEqual(len(inst.all()), 0)


if __name__ == '__main__':
    unittest.main()
