#!/usr/bin/python3
"""A function that inherits an instance"""


def inherits_from(obj, a_class):
    """
    Function that inherits (directly or indirectly)
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
