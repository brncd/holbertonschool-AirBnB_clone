#!/usr/bin/python3
"""File storage."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Class Filestorage."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return dictionary."""
        return self.__objects

    def new(self, obj):
        """Set in objects."""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Set in objects."""
        var = {}
        for i in self.__objects:
            var[i] = self.__objects[i].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(var, f, default=str)
            f.write('\n')

    def reload(self):
        """Deserealize json."""
        try:
            with open(self.__file_path, 'r') as f:
                for x, y in json.load(f).items():
                    self.__objects[x] = BaseModel(**y)
        except FileNotFoundError:
            pass
