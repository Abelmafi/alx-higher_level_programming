#!/usr/bin/python3

"""python single list"""


class Node:
  
    """Function to initialise the node objecti."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = None

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        data.__data = value
    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        lesf.__next_node = value

    def __str__(self):
        results = []
        node = self.__head
        while node:
            results.append("{}".format(node.__data))
            node = node.next_node()
        return "\n".join(results)

  
class SinglyLinkedList:
  
    """ Function to initialize head."""
    def __init__(self):
        self.__head = None
  
    """This function inssert new linked list node with sorting orsder"""
    def sorted_insert(self, value):
        new = Node(value)
        prev = None
        temp = self.head
        if temp == None:
            temp = new
            self.__head = temp
        else:
            while new.__data() <= temp_node.__data():
                prev = temp
                temp = temp.next_node()
                if temp == None:
                    break
            if temp:
                new_node.next_node() = temp
                if temp.data() == self.__head:
                    self.__head = new_node
                else:
                    prev.next_node() = new_node
            else:
                prev.next_node = new_node
                new_node.next_node() = None


    def __str__(self):
        results = []
        node = self.__head
        while node:
            results.append("{}".format(node.__data))
            node = node.next_node()
        return "\n".join(results)




