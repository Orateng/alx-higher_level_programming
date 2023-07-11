#!/usr/bin/python3
"""
A function that returns a dictionary
description with simple data structure
"""


def class_to_json(obj):
    """
    A function to return a dictionary description
    for JSON serialization of an object
    """
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
