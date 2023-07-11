#!/usr/bin/python3
"""A class MyInt that inherits from int"""


class MyInt(int):
    """The MyInt class as a rebel"""
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
