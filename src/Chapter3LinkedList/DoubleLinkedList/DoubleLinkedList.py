from Chapter3LinkedList.DoubleLinkedList.Node import Node


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insetAtBeginnig(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            newNode = Node(data)
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            current = self.head
            while current.getNext():
                current = current.getNext()
            newNode.setPrev(current)
            current.setNext(newNode)
            self.tail = newNode

    def getNode(self, index):
        node = self.head
        if node is None:
            return None
        for _ in range(index):
            node = node.getNext()
        return node

    def insert(self, data, n=0):
        if n == 0 or self.head is None:
            self.insetAtBeginnig(data)
        else:
            temp = self.getNode(n)
            if temp is None or temp.next is None:
                self.insertAtEnd(data)
            newNode = Node(data)
            temp.getPrev().next = newNode
            newNode.setPrev(temp.previous)
            newNode.setNext(temp)
            temp.setPrev(newNode)

    def __delete__(self, instance):
        current_node = self.getNode(instance)
        if current_node:
            # set previous node as current node's next
            current_node.getPrev().setNext(current_node.getNext())

            # if nextnode exis then next node of current node's
            # previous linker set of current node previous
            if current_node.getNext():
                current_node.getNext().setPrev(current_node.getPrev())

            # delete the existence of current node by setting None
            current_node.setData(None)
            current_node.setNext(None)
            current_node.setPrev(None)

    def delete_with_data(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if not temp.getPrev():
                    self.head = temp.getNext()

                if temp.getNext():

                    temp.getNext().setPrev(temp.getPrev())

                else:
                    self.tail = temp.getPrev()
            temp = temp.getNext()

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.getData())
            currentNode = currentNode.getNext()


if '__main__' == __name__:
    dll = DoubleLinkedList()
    dll.insetAtBeginnig(12)
    dll.insetAtBeginnig(123)
    dll.insetAtBeginnig(1234)
    dll.insertAtEnd(123111)
    dll.insert(21, 2)
    print()
    dll.printList()
    print('second index', dll.getNode(2).getData())
    dll.__delete__(2)
    dll.printList()
    dll.insertAtEnd(22)
    print()
    dll.printList()

    dll.delete_with_data(1234)
    print()
    dll.printList()
