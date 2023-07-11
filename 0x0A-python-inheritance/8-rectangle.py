#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """A defined class BaseGeometry"""
    def area(self):
        """Function that raises an exception"""
        raise Exception("area() is not implemented")

    """Function that returns a validation"""
    def integer_validator(self, name, value):
        """Condition for IndexErrors"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
