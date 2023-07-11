#!/usr/bin/python3
"""
A function that writes a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    The function appends a text
    file and number of characters
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
