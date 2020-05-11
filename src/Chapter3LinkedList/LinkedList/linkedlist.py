from Chapter3LinkedList.LinkedList.NodeSingleLinkedList import Node

class LinkedList:
    """Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at
     a contiguous location; the elements are linked using pointers."""

    def __init__(self):
        """it has head for the where the Linked List """
        self.length = 0
        self.head = None

    def getHead(self):
        """To get Head variable of the instance"""
        return self.head

    def listLength(self):
        # the current is the node so it has two attribute value and the data
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return  count

    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)


        # if list length is not zero then the node is zero
        newNode.setNext(self.head)
            
        self.head = newNode
        self.length  += 1

    def insertAtEnd(self,data):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(Node().setData(data))
        self.length += 1

    def insert(self,data,n =0):
        """ To insert the data in the linked list in given position."""
        if n > self.length:
            return None
        elif n == 0:
            self.insertAtBeginning(data)
        elif n == self.length:
            self.insertAtEnd(data)
        else :
            current = self.head
            newNode = Node()
            newNode.setData(data)
            for _ in range(n-1):
                current = current.getNext()
            newNode.setNext(current.getNext())
            current.setNext(newNode)
            self.length += 1

    def deleteFromBeginning(self):
        if self.length == 0:
            print('The List is empty')
        else:

            self.head = self.head.getNext()
            self.length -= 1

    def deleteFromEnding(self):
        if self.length == 0:
            print('The List is empty')
        else:
            currentNode = previousNode = self.head
            while currentNode != None:
                previousNode = currentNode
                currentNode = currentNode.getNext()
            previousNode.setNext(None)
            self.length -= 1

    def delete(self,n):
        if n > self.length:
            print('n is higher than length')
        elif n == 0:
            self.deleteFromBeginning()
        elif n == self.length:
            self.deleteFromEnding()
        else:
            current = self.head

            for _ in range(n-1):
                current = current.getNext()

            current.setNext(
                current.getNext().getNext()
            )

    def clear(self):
        self.head = None

    def printList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.getData())
            currentNode = currentNode.getNext()


if "__main__"== __name__:
    llist = LinkedList()

    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtBeginning(3)
    llist.insert(4,1)
    llist.printList()
    llist.delete(2)
    print()
    llist.printList()