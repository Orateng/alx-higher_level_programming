#!/usr/bin/python3
"""
Represents a square classs
"""


class Square:
    """
    Class for a square
    instatntiate a exception
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
