from src.Chapter4Stack.implementation.Stack import Stack
from src.Chapter6Trees.BinaryTreeNode import tree

tree = tree()

def traversePreOrder_DLR_recursive(result,root=tree,):
    # exit recursive condition
    if not root:
        return

    result.append(root.getData())
    print(result)
    traversePreOrder_DLR_recursive(result,root.left)
    traversePreOrder_DLR_recursive(result,root.right)

a = []
traversePreOrder_DLR_recursive(a)

def traversePreOrder_DLR_Stack(root = tree):
    stack = Stack()
    stack.push(root)
    res = []
    while stack.stack:
        res.append(root.data)
        print(res)
        if root.right: stack.push(root.getRight())
        if root.left : stack.push(root.getLeft())
        root = stack.pop()

print()
print()
traversePreOrder_DLR_Stack()