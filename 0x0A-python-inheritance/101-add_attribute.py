#!/usr/bin/python3
"""A function that adds an attribute to a object"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj,  attribute, value)
