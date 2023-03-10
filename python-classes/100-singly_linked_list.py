#!/usr/bin/python3
"""
    Singly linked list module
"""


class Node:
    """ Node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data setter"""
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """__str__ method"""
        linked_list = []
        tmp = self.__head
        while tmp is not None:
            linked_list.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(linked_list)
