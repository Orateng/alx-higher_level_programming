#!/usr/bin/python3
"""
A function tha returns the JSON
representation of an object(string)
"""


import json


def to_json_string(my_obj):
    """
    Function that returns json representation
    """
    return json.dumps(my_obj)
