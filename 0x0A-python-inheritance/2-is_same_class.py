#!/usr/bin/python3
"""
Function that returns True or False for
a specified object
"""


def is_same_class(obj, a_class):
    """
    A function that returns if
    object is exactly an instance
    """
    return type(obj) is a_class
