#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ary = my_list[:]
    for i, n in enumerate(ary):
        if n == search:
            ary[i] = replace
    return ary
