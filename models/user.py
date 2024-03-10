#!/usr/bin/python3
"""
=============================
Module with the user class
=============================
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class that represents a user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
