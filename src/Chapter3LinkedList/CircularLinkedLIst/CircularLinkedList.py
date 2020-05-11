from Chapter3LinkedList.CircularLinkedLIst.Node import Node


class CircularLinkedList:
    """
    Circular linked list is a linked list where all nodes are connected to form a circle.
    There is no NULL at the end. A circular linked list can be a singly circular
    linked list or doubly circular linked list.
    Advantages of Circular Linked Lists:
    1) Any node can be a starting point. We can traverse the whole list by starting from any point.
     We just need to stop when the first visited node is visited again.
    2) Useful for implementation of queue. Unlike this implementation, we don’t need to maintain
      two pointers for front and rear if we use circular linked list. We can maintain a pointer
      to the last inserted node and front can always be obtained as next of last.
    3) Circular lists are useful in applications to repeatedly go around the list.
       For example, when multiple applications are running on a PC, it is common for the operating
       system to put the running applications on a list and then to cycle through them, giving each
       of them a slice of time to execute, and then making them wait while the CPU is given to but
       another application. It is convenient for the operating system to use a circular list so
       that when it reaches the end of the list it can cycle around to the front of the list.
    4) Circular Doubly Linked Lists are used for implementation of advanced data
        structures like Fibonacci Heap.
    """

    def __init__(self):
        """ To initiate and To access the circular linked list we only need Head pointer """
        self.head = None

    def __len__(self):
        """ length of the circular linked list"""
        # to count the node we need to traverse the cll. but exit condition for loop is
        # not Null reference here but we use head pointer
        currentNode, counter = self.head, 0
        if currentNode:
            counter += 1
            while currentNode is not self.head:
                currentNode = currentNode.next()
                counter += 1
        return counter

    def insertNodeAtFront(self, data: object) -> None:
        """
                to insert Node at the front of the circular Linked List
                :param data: element we have to save in list
                :return: None
                """

        # 2 condition
        # 1st no node in the list
        currentNode = self.head
        newNode = Node(data)
        if not currentNode:
            # circular ll  connect it self for one node
            newNode.setNext(newNode)
            self.head = newNode

        # second condition is that we have nodes. in cll last node is pointing
        # to the head. by inserting new node at front, head is change to the
        # new Node. so last node also point to the new Node

        else:
            # for this first we have to traverse to the last node
            while currentNode.getNext() is not self.head:
                currentNode = currentNode.getNext()
            # change the last node  pointer to the new node
            currentNode.setNext(newNode)
            # change the newNode pointer to the previous head pointer
            # because previous head pointer is becomes second element in
            # cll now.
            newNode.setNext(self.head)
            # head pointer is newNode
            self.head = newNode

    def insertAtEnd(self, data: object) -> None:
        """
            to insert Node at the end of the circular Linked List
            :param data: element we want to save in list
            :return: None
        """

        # 2 condition
        # 1st no node in the list
        currentNode = self.head
        newNode = Node(data)
        if not currentNode:
            # circular ll  connect it self for one node
            newNode.setNext(newNode)
            self.head = newNode

        # second condition is that we have nodes. in cll last node is pointing
        # to the head. by inserting new node at end,last node is pointing to
        # current node and current Node points to head

        else:
            # for this first we have to traverse to the last node
            while currentNode.getNext() is not self.head:
                currentNode = currentNode.getNext()
            # change the last node  pointer to the new node
            currentNode.setNext(newNode)
            newNode.setNext(self.head)

    def insert(self, data: object, index: int) -> None:
        """ To insert the data in the linked list in given position."""
        if index == 0:
            self.insertNodeAtFront(data)
        else:
            current = self.head
            newNode = Node()
            newNode.setData(data)
            for _ in range(index - 1):
                current = current.getNext()
            if current.getNext() == self.head:
                self.insertNodeAtFront(data)
            else:
                newNode.setNext(current.getNext())
                current.setNext(newNode)

    def deleteFrontNode(self):
        """to delete the 1st node of the circular Linked List"""
        # use dummy variable to seek the understanding
        currentNode = self.head

        # traverse to the end then change the end pointer to second
        # list element
        while currentNode.getNext() is not self.head:
            currentNode = currentNode.getNext()

        # change the head pointer to the second pointer in the list
        self.head = self.head.getNext()
        currentNode.setNext(self.head)


    def deleteEndNode(self):
        """to delete the 1st node of the circular Linked List"""
        currentNode = self.head
        # traverse to the end and need previous pointer for the change to
        # the head that pointer
        previousNode = None
        while currentNode.getNext() is not self.head:
            currentNode, previousNode = currentNode.getNext(), currentNode
        previousNode.setNext(self.head)

    def printCircularList(self):
        """To print the data in the list"""
        currentNode = self.head
        print(currentNode.getData())
        while currentNode.getNext() is not self.head:
            currentNode = currentNode.getNext()
            print(currentNode.getData())


if "__main__" == __name__:
    cll = CircularLinkedList()
    cll.insertNodeAtFront(12)
    cll.insertNodeAtFront(112)
    cll.insertNodeAtFront(121)
    cll.insertNodeAtFront(122)
    cll.insertNodeAtFront(123)
    cll.insertAtEnd(222)
    cll.printCircularList()
    print()
    cll.insert(333, 3)
    cll.printCircularList()
    print()
    cll.deleteFrontNode()
    cll.printCircularList()
    print()
    cll.deleteEndNode()
    cll.printCircularList()
    """
    Bhav natmak nir bhalta
    karya kendrit lok
    Mitra kedriyata 
    """

