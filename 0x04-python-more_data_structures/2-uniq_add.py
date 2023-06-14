#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = sum([i for i in set(my_list) if i <= max(my_list)])
    return res
