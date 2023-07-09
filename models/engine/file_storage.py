#!/usr/bin/python3
"""File storage"""
import json
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """class Filestorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects"""
        name = obj.__class__.name__ + '.' + obj.id
        FileStorage.__objects[name] = obj

    def save(self):
        """sets in __objects"""
        var = {}
        for i in self.__objects:
            var[i] = self.__objects[i].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dump(var, default=str))

    def reload(self):
        """deserealizes"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for x, y in json.load(f).items():
                    FileStorage.__objects[x] = BaseModel(**y)
        except FileNotFoundError:
            pass
