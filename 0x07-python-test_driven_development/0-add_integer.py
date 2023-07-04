#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an inter")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    gee = (a + b)
    return (gee)
