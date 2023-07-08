#!/usr/bin/python3
""Console""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    ""HBNBCommand""

    prompt = "(hbnb)"
    classes = {"User": User, "BaseModel": BaseModel,
               "State": State, "City": City, "Amenity": Amenity,
               "Place": Place, "Review": Review}

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command"""
        print()
        return True

    def emptyline(self):
        """An empty line shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
