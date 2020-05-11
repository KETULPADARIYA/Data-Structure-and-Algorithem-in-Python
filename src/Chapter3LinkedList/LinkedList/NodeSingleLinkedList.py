class Node:
    """
    The unit element of the list
    """

    def __init__(self,data=None):
        """
                Node has two varible one data for value and pointer that points to the next
                element in the list
                """

        self.data = data
        self.next = None

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
        self.next =  Next

    def hasNext(self):
        """TO check the Node has next Node or not"""
        # hasNext means value is not None
        return self.next != None
