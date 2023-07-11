#!/usr/bin/python3
"""A function that adds an attribute to a object"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute"""
    if "__dict__" not in dir(obj):
        raise TypeError("cant add new attribute")
    if "__slots__" in dir(obj):
        raise TypeError("cant add a new attribute")
    else:
        setattr(obj, attribute, value)
