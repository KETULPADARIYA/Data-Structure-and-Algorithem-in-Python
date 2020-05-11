from src.Chapter4Stack.implementation.Stack import Stack


def evaluate_post_fix(expression):
    stack = Stack()
    for element in expression:
        if element not in list('+-*/'):
            stack.push(element)
        else:
            B = stack.pop()
            A = stack.pop()
            stack.push(str(eval(A+element+B)))
    return int(stack.pop())