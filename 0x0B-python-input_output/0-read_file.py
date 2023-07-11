#!/usr/bin/python3
"""A function that reads a test file(UTF8)"""


def read_file(filename=""):
    """The function that prints in stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
