#!/usr/bin/python3
"""File storage"""
import json
from models.user import User
from models import BaseModel


class FileStorage:
    """class Filestorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects"""
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """sets in __objects"""
        var = {}
        for i in self.__objects:
            var[i] = self.__objects[i].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(var, f, default=str)

    def reload(self):
        """deserealizes"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for x, y in json.load(f).items():
                    FileStorage.__objects[x] = BaseModel(**y)
        except FileNotFoundError:
            pass
