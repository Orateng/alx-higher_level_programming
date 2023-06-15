#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    df = my_list[:]
    return (list(map((lambda x: x * 4), df)))
