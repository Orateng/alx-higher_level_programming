#!/usr/bin/python3
"""module subclass rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


"""A class for a rectangle"""


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {} / {}".format(self.__width, self.__height)
