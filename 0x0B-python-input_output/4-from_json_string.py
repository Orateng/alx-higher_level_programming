#!/usr/bin/python3
"""
A function that returns object
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Function that returns json string
    """
    return json.loads(my_str)
