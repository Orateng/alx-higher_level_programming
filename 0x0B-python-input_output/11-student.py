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

    def to_json(self, attrs=None):
        """
        A Function that retrieves a dictionary
        representation of a Student class
        """

        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}
            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
                return d_list

        return obj

    def reload_from_json(self, json):
        """
        Function method that replaces
        all attributes of Student class
        """
        for atr in json:
            self.__dict__[atr] = json[atr]
