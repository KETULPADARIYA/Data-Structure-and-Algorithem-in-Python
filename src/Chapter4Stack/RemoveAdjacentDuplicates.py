from src.Chapter4Stack.implementation.Stack import Stack

def remove_adjacent_duplicates(text):
    stk = Stack()
    for character in text:
        if stk.IsEmpty() or stk.top() != character:
            stk.push(character)
        else:
            stk.pop()
    return ''.join(stk.stack)