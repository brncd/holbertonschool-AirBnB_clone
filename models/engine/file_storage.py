#!/usr/bin/python3
"""Store first object."""
import json


class FileStorage:
    """FileStorage class."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                    "Amenity": Amenity, "City": City, "Place": Place,
                    "Review": Review}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                FileStorage.__objects[key] = classes[value["__class__"]](
                    **value)
        except FileNotFoundError:
            pass
