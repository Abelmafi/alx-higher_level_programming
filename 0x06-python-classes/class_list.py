#!/usr/bin/python3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push_head(self, data):
        new_node = Node(data)
        prevnode = None
        node = self.head
        if node == None:
            node = new_node
            self.head = node
        else:
            while new_node.data >= node.data:
                prevnode = node
                node = node.next
                if node == None:
                    break
            if node:
                new_node.next = node
                if node == self.head:
                    self.head = new_node
                else:
                    prevnode.next = new_node
            else:
                prevnode.next = new_node
                new_node.next = None

    def push_tail(self, data):
        new_node = Node(data)
        if new_node.data < 0:
            node = self.head
            new_node.next = node
            self.head = new_node

    def __str__(self):
        pieces = []
        temp = self.head
        while temp:
            pieces.append("{}".format(temp.data))
            temp = temp.next
        return "\n".join(pieces)

if __name__ == '__main__':
    
    llist = LinkedList()

    String = [8, 7, 1, -2, 6, -5, 3, 4]
    for node in String:
        llist.push_head(node)
    print(llist)


