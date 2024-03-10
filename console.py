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
from models import storage



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
        Creates a new instance of class given
        """
        args_splitted = args.split()

        if not err_prints(args_splitted):
            return
        else:
            obj = CLASSES[args_splitted[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """
        Shows onstance with given id
        """
        args_splitted = args.split()
        if not err_prints(args_splitted, is_id=True):
            return
        else:
            objs = storage.all()
            key_given = "{}.{}".format(args_splitted[0], args_splitted[1])
            for key, value in objs.items():
                if key_given == key:
                    print(value)
                    return
            print("** no instance found **")


    def do_destroy(self, args):
        """
        destroy certain instance
        """
        args_splitted = args.split()
        if not err_prints(args_splitted, is_id=True):
            return
        else:
            objs = storage.all()
            key_given = "{}.{}".format(args_splitted[0], args_splitted[1])
            for key, value in objs.items():
                if key_given == key:
                    del objs[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """
        Shows all instances
        """

        args_splitted = args.split()
        objs = storage.all()

        if len(args_splitted) < 1:
            print(["{}".format(str(value)) for key, value in objs.items()])
            # print([obj.all() for obj in objs])

        else:
            if args_splitted[0] not in CLASSES.keys():
                print("** class doesn't exist **")
            else:
                print(["{}".format(str(value)) for key, value in objs.items() if value['__class__'] == args_splitted[0]])
        



def err_prints(args, is_id = False):

        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in CLASSES.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and is_id:
            print("** instance id missing **")
            return False
        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
