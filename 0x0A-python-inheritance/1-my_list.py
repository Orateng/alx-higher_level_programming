#!/usr/bin/python3
"""A class for MyList class that inherits from list"""


class MyList(list):
    """Mylist class method for sorting in ascending order"""
    def print_sorted(self):
        """Function that sorts list attributes"""
        sorted_list = sorted(self)
        print(sorted_list)
