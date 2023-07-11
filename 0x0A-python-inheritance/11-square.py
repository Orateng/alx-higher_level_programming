#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(BaseGeometry):
    """Represents a square"""

    def __init__(self, size):
        """A rectangle function"""
        self.integer_validator("size", size)
        self.__size = size

    """A function that prints a description of the square"""
    def __str__(self):
        """The function for a description of a square"""
        return "[Square] " + str(self.__size) + '/' + str(self.__size)

    """A function for the area of a square"""
    def area(self):
        """The function for a area of a square"""
        return self.__size ** 2
