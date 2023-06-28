#!/usr/bin/python3
"""
Represents a square classs
"""


class Square:
    """
    Class for a square
    instatntiate a exception
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Property for the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout, the square with a character (#)"""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print("")
