#!/usr/bin/python3
"""
=============================
Module with the city class
=============================
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    class that represents a city
    """

    state_id = ""
    name = ""
