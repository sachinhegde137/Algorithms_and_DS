import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


def has_cycle(head):
    visited_nodes = []

    current = head
    while current:
        if current in visited_nodes:
            return True
        visited_nodes.append(current)
        current = current.next
    return False

if __name__ == '__main__':

    index = int(input())
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    extra = SinglyLinkedListNode(-1)
    temp = llist.head

    for i in range(llist_count):
        if i == index:
            extra = temp

        if i != llist_count-1:
            temp = temp.next

    temp.next = extra

    result = has_cycle(llist.head)
    if result:
        print("The linked list is circular.")
    else:
        print("The linked list is NOT circular.")

