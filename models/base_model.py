#!/usr/bin/python3
"""
=============================
Module with the class Rectangle
=============================
"""


import uuid
from datetime import datetime


class BaseModel:
    """base class for the project"""

    def __init__(self):
        """
        The constructor of the class BaseModel
        """
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
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(timespec='microseconds'),
            "updated_at": self.updated_at.isoformat(timespec='microseconds'),
            **self.__dict__,
        }