#!/usr/bin/python3
"""
Defines Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """defines review to look for"""

    place_id = ""
    user_id = ""
    text = ""
