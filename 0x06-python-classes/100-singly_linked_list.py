#!/usr/bin/python3

"""python single list"""


class Node:
    """Function to initialise the node objecti."""

    def __init__(self, data, next_node=None):
        """Initilising object variables.

        Args:
            data (int): linked list data.
            next_node (str): linked list next node.
        """
        self.data = data
        self.next_node = None

    @property
    def data(self):
        """Get linked list node data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get linked list next nde."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    """ Function to initialize head."""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ insert linked list node in increasing order."""
        new_node = Node(value)
        prev = None
        temp = self.__head
        if temp is None:
            temp = new_node
            self.__head = temp
        else:
            while new_node.data >= temp.data:
                prev = temp
                temp = temp.next_node
                if temp is None:
                    break
            if temp:
                new_node.next_node = temp
                if temp == self.__head:
                    self.__head = new_node
                else:
                    prev.next_node = new_node
            else:
                prev.next_node = new_node
                new_node.next_node = None

    def __str__(self):
        """print linked list."""
        results = []
        node = self.__head
        while node:
            results.append("{}".format(node.data))
            node = node.next_node
        return "\n".join(results)
