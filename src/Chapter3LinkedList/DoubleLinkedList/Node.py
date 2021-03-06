class Node:
    def __init__(self, data,previous =None,next = None):
        """
            Node has three variable one data for value and two pointer that points to the next
            element in the list
        """

        self.data = data
        self.previous = previous
        self.next = next

    def getData(self):
        """To get data variable of the instance"""
        return self.data

    def setData(self, data):
        """To set the value of data variable"""
        self.data = data

    def getNext(self):
        """To get Next variable of the instance"""
        return self.next

    def setNext(self, Next):
        """To set the value of Next variable"""
        self.next = Next

    def hasNext(self):
        """TO check the Node has next Node or not"""
        # hasNext means value is not None
        return self.next is not None

    def getPrev(self):
        """To get Next variable of the instance"""
        return self.previous

    def setPrev(self, previous):
        """To set the value of Next variable"""
        self.previous = previous

    def hasPrev(self):
        """TO check the Node has next Node or not"""
        # hasNext means value is not None
        return self.previous is not None

    def __str__(self):
        return "Node[ data = %s ]" % self.data

