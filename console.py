#!/usr/bin/python3
"""
=============================
Module with the CMD class
=============================
"""

import cmd
import os
import json
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



CLASSES = {"BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review}


class HBNBCommand(cmd.Cmd):
    """
    CMD Class Contains all functions that will be excuted
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """

        return True

    def do_EOF(self, arg):
        """End of File command to exit the program
        """

        print()
        return True

    def emptyline(self):
        """Ensures that an empty line + ENTER shouldn’t
        execute anything"""

        return False

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        """
#         create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
# If the class name is missing, print ** class name missing ** (ex: $ create)
# If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        obj = args.split()
        if len(obj) < 1:
            print("** class name missing **")
        else:
            if obj.__class__.__name__ not in CLASSES.keys():
                print("** class doesn't exist **")
            else:
                obj.save()
                print(obj.id)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
