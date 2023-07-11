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
