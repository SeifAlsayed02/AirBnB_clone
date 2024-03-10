#!/usr/bin/python3
"""
=============================
Module with the CMD class
=============================
"""

import cmd
import os
import json

class HBNBCommand(cmd.Cmd):
    """
    CMD Class Contains all functions that will be excuted
    """

    prompt = "(hbnb) "

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()