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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
