from src.Chapter4Stack.implementation.Stack import Stack

def largest_area(hist_array):
    stk = Stack()

    i=max_area = 0
    while len(hist_array)>i:
        if  stk.IsEmpty() or hist_array[i] >= hist_array[stk.top()]:
            stk.push(i)
            i += 1
        else:
            poped_item = stk.pop()
            width = i - stk.top() - 1 if stk.stack else i
            max_area = max(max_area, width * hist_array[poped_item])

    while not stk.IsEmpty():
        poped_item = stk.pop()
        width = i - stk.top() - 1 if stk.stack else i
        max_area = max(max_area, width * hist_array[poped_item])

    return max_area