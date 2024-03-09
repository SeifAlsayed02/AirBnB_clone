#!/usr/bin/python3
"""
=============================
Module with the class Rectangle
=============================
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    base class for the project
    """

    def __init__(*args, **kwargs):
        """
        The constructor of the class BaseModel
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "updated_at" or key == "created_at":
                    str_value = datetime.fromisoformat(value)
                setattr(self, key, str_value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        The string representation of the class BaseModel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
