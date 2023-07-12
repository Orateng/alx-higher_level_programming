#!/usr/bin/python3
"""
A function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    res_line = []
    """Function for inserting a string"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != - 1:
                res_line += [new_string]

    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(res_line))