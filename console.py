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
import models


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

    def do_show(self, line):
        """Print str repr based on class name and id."""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.l_classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Delete a instance."""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.l_classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Print str repr of instances based on the class name."""
        args = line.split()
        if not line:
            for key, value in models.storage.all().items():
                print(value)
        elif args[0] not in HBNBCommand.l_classes.keys():
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if args[0] in key:
                    print(value)

    def do_update(self, line):
        """Update an instance based on the class name and id."""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.l_classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(models.storage.all()[key], args[2], args[3])
                    models.storage.all()[key].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
