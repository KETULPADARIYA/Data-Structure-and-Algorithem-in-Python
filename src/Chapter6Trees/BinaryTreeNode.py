class BinaryTreeNode:
    def __init__(self,data,left =None,right = None):
        self.data = data # root data
        self.left = None
        self.right = None

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setLeft(self,object):
        self.left = object

    def setRight(self,object):
        self.right = object

    def getRight(self):
        return self.right

    def getLeft(self):
        return  self.left



#### BinaryTreeNode Example
# wrong its like we are storing the numbers
def WRONG_EXAMPLE():
    root0 = BinaryTreeNode(1,2,4)
    root1 = BinaryTreeNode(2,5,3)
    root2 = BinaryTreeNode(4,6,7)
    root3 = BinaryTreeNode(5,None,None)
    root4 = BinaryTreeNode(3,None,None)
    root5 = BinaryTreeNode(6,None,None)
    root6 = BinaryTreeNode(7,None,None)


def tree():
    root = BinaryTreeNode(1)
    root1 = BinaryTreeNode(2)
    root2 = BinaryTreeNode(3)
    root3 = BinaryTreeNode(4)
    root4 = BinaryTreeNode(5)
    root5 = BinaryTreeNode(6)
    root6 = BinaryTreeNode(7)

    root1.setLeft(root4)
    root1.setRight(root2)
    root3.setLeft(root5)
    root3.setRight(root6)
    root.setRight(root3)
    root.setLeft(root1)
    return root