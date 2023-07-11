#!/usr/bin/python3
"""A class BaseGeometry that creates a rectangle subclass"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


"""A class for a rectangle"""


class Rectangle(BaseGeometry):
    """The rectangle class"""

    """A function that creates a rectangle"""
    def __init__(self, width, height):
        """A rectangle function"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
