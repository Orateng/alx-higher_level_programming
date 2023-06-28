#!/usr/bin/python3
"""
Represents a node classs
"""


class Node:
    """
    Class for a node
    instatntiate a exception
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property for the size"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Property for the position"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A class that defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new = self.__head
            while (new.next_node is not None and
                    new.next_node.data < value):
                new = new.next_node
            new_node.next_node = new.next_node
            new.next_node = new_node

    def __str__(self):
        """Define the print of a SinglyLinkedList"""
        values = []
        new = self.__head
        while new is not None:
            values.append(str(new.data))
            new = new.next_node
        return ('\n'.join(values))
