#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list1 = list(map(lambda x: list(map(lambda y: (y**2), x)), matrix))
    return(list1)
