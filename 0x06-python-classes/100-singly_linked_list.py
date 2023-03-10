#!/usr/bin/python3
"""Singly Linked Lists module.
This module contains methods about the creation and hendling of
SinglyLinkedList and Node objects.
"""


class Node():
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Sets the necessary attributes for the Node object.
        Args:
            data (int): the value of the node
            next_node (Node): the next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data value of a node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next node of the current node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Defines a singly linked list"""

    def __init__(self):
        """Sets the necessary attributes for the SinglyLinkedList object."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
