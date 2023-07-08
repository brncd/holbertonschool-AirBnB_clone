#!/usr/bin/python3
"""Console."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand."""

    prompt = "(hbnb)"
    classes = {"User": User, "BaseModel": BaseModel,
               "State": State, "City": City, "Amenity": Amenity,
               "Place": Place, "Review": Review}

    def do_quit(self, arg):
        """Quit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command."""
        print()
        return True

    def emptyline(self):
        """Empty line."""
        pass

    def do_create(self, line):
        """Create new instance of BaseModel."""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.l_classes.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.l_classes[args[0]]()
            obj.save()
            print(obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
