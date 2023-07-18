#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for Square that
    inherits from the class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes for the size of a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns objects that represents a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    """Property of size for class Square"""
    def size(self):
        return self. width

    @size.setter
    """Setter of size for class Square"""
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """A function to update the Square with key arguments"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Representation of the Square in a dictionary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
