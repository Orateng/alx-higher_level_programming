#!/usr/bin/python3
"""
A class that defines a student by Student
"""


class Student:
    """The class for defining a student"""
    def __init__(self, first_name, last_name, age):
        """Function that initialize method
            for Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A Function that retrieves a dictionary
        representation of a Student class
        """
        return self.__dict__.copy()
