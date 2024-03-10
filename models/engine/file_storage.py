#!/usr/bin/python3
"""
=============================
Module with the file storage class
=============================
"""

import os
import json
# from models.base_model import BaseModel


class FileStorage:
    """
    class that serializes instances to
    a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key_class_id = "{}.{}".format(obj.__class__.__name__, obj.id)

        FileStorage.__objects[key_class_id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: value.to_dict() for key, value in FileStorage.__objects.items()}, f)




    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    FileStorage.__objects = json.load(f)
                except:
                    FileStorage.__objects = {}
