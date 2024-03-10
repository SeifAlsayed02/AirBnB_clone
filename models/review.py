#!/usr/bin/python3
"""
=============================
Module with the review class
=============================
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class that represents a review
    """

    place_id = ""
    user_id = ""
    text = ""
