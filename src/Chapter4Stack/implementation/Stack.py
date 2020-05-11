"""
Author: Ketul Padariya

array has fix length and stack is used to store element as stack.
"""


class Stack:
    """LILO or FIFO"""

    def __init__(self):
        self.stack = []

    def push(self, element: object):
            self.stack.append(element)

    def pop(self):
        """ To give last element of the stack and remove it from the stack"""
        if self.stack:
            return self.stack.pop()
        else:
            print('Stack UnderFlow')

    def size(self):
        """ return the length of stack"""
        return len(self.stack)

    def IsEmpty(self):
        """ return True if stack is empty else returns False """
        return True if not self.stack else False

    def top(self):
        """ Returns the top of the element"""
        return self.stack[-1] if self.stack else None

    def printStack(self):
        print(self.stack)

# if "__main__"==__name__:
#     stk = Stack()
#     stk.pop()
#     stk.push(2)
#     stk.push(3)
#     stk.printStack()
#     print("poped",stk.pop())
#     stk.printStack()