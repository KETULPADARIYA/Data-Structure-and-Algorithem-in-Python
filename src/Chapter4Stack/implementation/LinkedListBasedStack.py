"""
Author: Ketul Padariya

array has fix length and stack is used to store element as stack.
"""
from typing import Iterable

from Chapter3LinkedList.LinkedList.NodeSingleLinkedList import Node


class Stack:
    """FIFO"""

    def __init__(self, data: Iterable or None = None):
        self.head:Node or None = None
        if data:
            for i in data:
                self.push(i)


    def push(self, element: object):
        NewNode = Node(element)
        NewNode.setNext(self.head)
        self.head = NewNode

    def pop(self):
        """ To give last element of the stack and remove it from the stack"""
        if self.head == None:
            raise IndexError
        temp:object = self.head.getData()
        self.head.setNext(self.head.getNext())
        return temp

    def IsEmpty(self):
        """ return True if stack is empty else returns False """
        return False if self.head else True

    def top(self):
        """ Returns the top of the element"""
        return self.head.getData()
list

if "__main__"==__name__:
    stk = Stack()
    stk.pop()
    stk.push(2)
    stk.push(3)
    print("poped",stk.pop())
