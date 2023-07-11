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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {} / {}".format(self.__width, self.__height)
