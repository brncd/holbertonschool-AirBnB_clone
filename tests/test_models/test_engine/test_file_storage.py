#!/usr/bin/python3
""" file storage tests """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FilestorageClass(unittest.TestCase):
    """test file storage"""
    def test_filepath(self):
        """file path is set on file.json"""
        var = FileStorage()
        avar = var._Filestorage__file_path
        self.assertEqual(avar, "file.json")

    def test_everithing(self):
        var = FileStorage()
        var.all().clear()
        var.reload()
        self.assertTrue(len(var.all()) > 0)
