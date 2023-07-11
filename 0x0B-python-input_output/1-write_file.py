#!/usr/bin/python3
"""The that returns a string"""


def write_file(filename="", text=""):
    """A function that prints the number of characters written"""
    with open(filename, "w", encoding="utf=8") as f:
        return f.write(text)
